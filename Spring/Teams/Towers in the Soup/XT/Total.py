import totalData
import totalData as TD

def total(a,b,c):
    return a+b+c

totalGrossIncomes = total(TD.totalResidentialIncome,
                          TD.totalCommercialIncome,
                          TD.totalManufacturingIncome)

totalVacancy = total(TD.totalResidentialVacancy,
                     TD.totalCommercialVacancy,
                     TD.totalManufacturingVacancy)

totalExpenses = total(TD.totalPropertyOperationalExpenses,
                      TD.totalPropertyRealEstateTaxes,
                      TD.totalPropertyReplacementReserve)

totalDepreciationCost = total(TD.residentialDepreciation,
                              TD.commercialDepreciation,
                              TD.manufacturingDepreciation)
print(totalGrossIncomes)
print(totalVacancy)
print(totalExpenses)
print(totalDepreciationCost)



def totalGrossIncomes(totalResidentialIncome,totalCommercialIncome,totalManufacturingIncome):
    return totalResidentialIncome + totalCommercialIncome + totalManufacturingIncome

def totalVacancy(totalResidentialVacancy,totalCommericialVacancy,totalManufacturingVacancy):
    return totalResidentialVacancy + totalCommericialVacancy + totalManufacturingVacancy

def totalExpenses(totalPropertyOperationalEXpenses,totalPropertyRealEstateTaxes,toalPropertyReplacementReserve):
    return totalPropertyOperationalEXpenses + totalPropertyRealEstateTaxes + toalPropertyReplacementReserve

def totalDepreciationCost(totalResidentialDepreciation,totalCommercialDepreciation,totalManufacturingDepreciation):
    return totalResidentialDepreciation + totalCommercialDepreciation + totalManufacturingDepreciation





dict_GrossIncom = {'totalResidentialIncome':TD.totalResidentialIncome,
                 'totalCommercialIncome':TD.totalCommercialIncome,
                 'totalManufacruingIncome':TD.totalManufacturingIncome}

dict_Vacancy = {'totalResidentialVacancy':TD.totalResidentialVacancy,
                 'totalCommercialVacancy':TD.totalCommercialVacancy,
                 'totalManufacruingVacancy':TD.totalManufacturingVacancy}

dict_Expenses = {'totalPropertyOperationalExpenses':TD.totalPropertyOperationalExpenses,
                 'totalPropertyRealEstateTaxes':TD.totalPropertyRealEstateTaxes,
                 'totalPropertyReplacementReserve':TD.totalPropertyReplacementReserve}

dict_Depreciation = {'residentialDepreciation':TD.residentialDepreciation,
                 'commercialDepreciation':TD.commercialDepreciation,
                 'manufacturingDepreciation':TD.manufacturingDepreciation}

print(dict_GrossIncom)
print(dict_Vacancy)
print(dict_Expenses)
print(dict_Depreciation)








