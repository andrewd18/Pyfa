# eliteBonusLogisticShieldTransferCapNeed2
#
# Used by:
# Ship: Scimitar
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Shield Booster",
                                  "capacitorNeed", ship.getModifiedItemAttr("eliteBonusLogistics2"), skill="Logistics")
