# scriptMissileGuidanceComputerMissileVelocityBonusBonus
#
# Used by:
# Charges from group: Missile Guidance Script (2 of 2)
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("missileVelocityBonus", module.getModifiedChargeAttr("missileVelocityBonusBonus"))
