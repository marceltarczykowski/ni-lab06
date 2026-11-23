from src.models import Parameters
from src.manager import Manager


def test_tenant_settlements_sum_matches_apartment_costs():
    manager = Manager(Parameters())
    apartment_settlement = manager.get_settlement("apart-polanka", 2025, 1)
    tenant_settlements = manager.create_tenants_settlements(apartment_settlement)
    
    total_tenants_due = sum(ts.total_due_pln for ts in tenant_settlements)
    
    assert abs(total_tenants_due - apartment_settlement.total_due_pln) < 0.01


def test_get_debtors_no_debtors():
    manager = Manager(Parameters())
    debtors = manager.get_debtors("apart-polanka", 1, 2025)
    
    assert debtors == []


def test_get_debtors_with_debtors():
    manager = Manager(Parameters())
    manager.tenants["tenant-1"].rent_pln = 3000.0
    
    debtors = manager.get_debtors("apart-polanka", 1, 2025)
    
    assert "Jan Nowak" in debtors
    assert len(debtors) == 1
