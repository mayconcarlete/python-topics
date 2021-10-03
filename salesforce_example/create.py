async def _create_pagarme_client(sf_account_id, company_id, **kwargs):
    clean_document = kwargs.get("clean_document")
    clean_zipcode = kwargs.get("clean_zipcode")
    account = kwargs.get("account")
    address = kwargs.get("address")
    contact = kwargs.get("contact")
    bank_account = kwargs.get("bank_account")
    company_info = kwargs.get("company_info")
    # closer_id = kwargs.get("closer_id")
    # _logger.info(f"closer_id: {closer_id}")

    search_account = await sf.query(
        f"""
            SELECT "Id" from "Account"
            where ("cnpj__c" = '{clean_document}') and
            "RecordTypeId" = '{RECORD_TYPE_ACCOUNTS['pagar_me_client']}' and
            "AffiliationId__c" = '{company_id}'
        """
    )
    if search_account.get("totalSize"):
        message = f"Pagarme Client - {clean_document} - already exists!"
        _logger.info(message)
        try:
            sf_id = search_account["records"][0]["Id"]
            # create an event
            await _create_event(sf_id, "pagarme_client_recovered")
            return sf_id
        except (IndexError, KeyError):
            message = "Can't recovery Pagarme Client Id."
            _logger.error(message)
            raise Forbidden(message)

    company_full_name = account.get("full_name")
    pagarme_code = account.get("pagarme_code")

    account_name = f"{company_full_name} - {company_id}"

    if isinstance(pagarme_code, str):
        account_name += f" - {pagarme_code}"

    # create an account (pagarme client)
    payload = {
        "Name": account_name,
        "ParentId": sf_account_id,
        "RecordTypeId": RECORD_TYPE_ACCOUNTS["pagar_me_client"],
        "AffiliationId__c": company_id,
        "BillingStreet": address.get("street"),
        "BillingCity": address.get("city"),
        "BillingState": address.get("state"),
        "BillingPostalCode": clean_zipcode,
        "BillingCountry": "Brasil",
        "Phone": contact.get("phone_number"),
        "cnpj__c": clean_document,
        "cpf_cnpj__c": clean_document,
        "ClientStatus__c": "Active",
        "AccountStatus__c": "Active",
        "legal_name__c": account.get("name"),
        "Razao_Social__c": account.get("name"),
        "BankAccountBankName__c": bank_account.get("bank_code"),
        "BankAccountType__c": bank_account.get("type"),
        "BankAccountAgencyNumber__c": bank_account.get("agencia"),
        "BankAccountAgencyDigit__c": bank_account.get("agencia_dv"),
        "BankAccountNumber__c": bank_account.get("conta"),
        "BankAccountDigit__c": bank_account.get("conta_dv"),
        "sales_channel_name__c": SALES_CHANNEL_NAME.get(
            company_info.get("seller_id", None),
            "Pagar.me MEI",
        )
    }

    _logger.info(payload)
    response = await sf.Account.create(payload)

    if not response.get("success"):
        message = "The Pagarme Client wasn't created."
        _logger.error(message)
        raise RequestTimeout(message)

    # register creation event
    sf_id = response.get("id")
    await _create_event(sf_id, "pagarme_client_created", payload)

    # return id
    return sf_id
