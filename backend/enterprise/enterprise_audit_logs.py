class EnterpriseAuditLogs:

    def log_event(
        self,
        organization_id: int,
        event_type: str
    ):
        return True


enterprise_audit_logs = EnterpriseAuditLogs()