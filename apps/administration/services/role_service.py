class RoleService:
    # Standard roles configured per the system design
    AVAILABLE_ROLES = [
        {"id": 1, "name": "Super Admin", "description": "Full access to all modules and configurations"},
        {"id": 2, "name": "Admin", "description": "Operational access across portal"},
        {"id": 3, "name": "Treasurer", "description": "Financial and billing management access"},
        {"id": 4, "name": "Resident", "description": "Portal access for apartment owners/tenants"},
        {"id": 5, "name": "Security", "description": "Security personnel portal access"},
    ]

    @classmethod
    def get_all_roles(cls):
        return cls.AVAILABLE_ROLES