# shipEnergyNeutralizerRangeBonusAF2
#
# Used by:
# Ship: Malice
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Destabilizer",
                                  "energyDestabilizationRange", ship.getModifiedItemAttr("shipBonus2AF"), skill="Amarr Frigate")
