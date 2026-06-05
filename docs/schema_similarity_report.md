# Schema to Component Semantic Similarity Report

This report lists the **Cosine Similarity** between the natural language descriptions of the enriched Schema Classes and the database component embeddings.

- **Source CSV:** `enriched_schema_classes.csv` (57 classes)
- **Vector DB Collection:** `groq_schema_collection` (315 components)
- **Embedding Model:** `all-MiniLM-L6-v2` (SentenceTransformers)
- **Cosine Similarity Formula:** `1 - (L2_Distance / 2.0)`

---

## Executive Summary Table

| # | Schema Class | Best Match Target | Top Cosine Similarity |
|---|---|---|---|
| 1 | [`ReverseCA`](#reverseca) | `ReversalProvision` -> `TDSValue` | **0.8427** |
| 2 | [`Bill_I`](#billi) | `BillHead` -> `totalrate` | **0.8579** |
| 3 | [`Bill_H`](#billh) | `PO&IPVsBill` -> `Bill` | **0.8719** |
| 4 | [`PrevBill`](#prevbill) | `PrevBill` -> `Basevalue` | **0.8536** |
| 5 | [`PO&IP_Status`](#poipstatus) | `PO&IPVsBill` -> `POorIPRate` | **0.8302** |
| 6 | [`Bill_Item`](#billitem) | `Bill_Item` -> `headaddlcharge` | **0.8720** |
| 7 | [`CostAllocationMaster`](#costallocationmaster) | `POCostAllocation` -> `TCostAllocationValue` | **0.8189** |
| 8 | [`BillCostAllocation1`](#billcostallocation1) | `BillCostAllocation` -> `AmountinLocalCurrency2` | **0.8740** |
| 9 | [`TCostAllocationValue`](#tcostallocationvalue) | `TCostAllocationValue` -> `TCostAllocationValue` | **0.8689** |
| 10 | [`AP`](#ap) | `AP` -> `SNO` | **0.8242** |
| 11 | [`BillWF`](#billwf) | `BillWF` -> `DocumentValue` | **0.8631** |
| 12 | [`AD`](#ad) | `AD` -> `CummThresholdLimit` | **0.8274** |
| 13 | [`IM`](#im) | `IM` -> `PercentageofTDS` | **0.8104** |
| 14 | [`VM`](#vm) | `VM` -> `SNO` | **0.8223** |
| 15 | [`ProcessedTDSAmtinGSE`](#processedtdsamtingse) | `ProcessedTDSAmtinGSE` -> `amountinlocalcurrency` | **0.7903** |
| 16 | [`ReversalTDS`](#reversaltds) | `ReversalTDS` -> `Value` | **0.8621** |
| 17 | [`ReversalProvisionExpAcc`](#reversalprovisionexpacc) | `ReversalProvisionExpAcc` -> `ProvisionValue` | **0.8680** |
| 18 | [`ReversalProvision`](#reversalprovision) | `ReversalProvision` -> `ProvisionValue` | **0.8866** |
| 19 | [`ProvisionReversalAccountingJournal`](#provisionreversalaccountingjournal) | `ProvisionReversalCostAllocation` -> `Value` | **0.8289** |
| 20 | [`ExpAccBill_I`](#expaccbilli) | `ExpAccBill_I` -> `Value` | **0.8709** |
| 21 | [`GSTAccBill_I`](#gstaccbilli) | `GSTAccBill_I` -> `AmountinTransactionCurrency` | **0.9012** |
| 22 | [`ExpAccBill_I_GST`](#expaccbilligst) | `ExpAccBill_I_GST` -> `BillBaseValue` | **0.8959** |
| 23 | [`TDSAccBill_I`](#tdsaccbilli) | `TDSAccBill_I` -> `AmountinLocalCurrency` | **0.8834** |
| 24 | [`ExpAccBill_I_TDS`](#expaccbillitds) | `ExpAccBill_I_TDS` -> `AmountinTransactionCurrency` | **0.8575** |
| 25 | [`RoundOffAcc`](#roundoffacc) | `Bill_H` -> `RoundOffValue` | **0.8723** |
| 26 | [`CrAccBill_I`](#craccbilli) | `CrAccBill_I` -> `AmountinLocalCurrency` | **0.8779** |
| 27 | [`AccountingJournal`](#accountingjournal) | `ErrorDetection` -> `TotalBillBaseValue` | **0.8119** |
| 28 | [`ProvisionReversalCostAllocation`](#provisionreversalcostallocation) | `BillCostAllocation` -> `AmountinLocalCurrency2` | **0.8664** |
| 29 | [`BillCostAllocation`](#billcostallocation) | `BillCostAllocation` -> `AmountinLocalCurrency2` | **0.8931** |
| 30 | [`AmortizeBill_I`](#amortizebilli) | `AmortizeBill_I` -> `BillBasevalue` | **0.8956** |
| 31 | [`PO&IPVsBill`](#poipvsbill) | `PO&IPVsBill` -> `Different` | **0.8834** |
| 32 | [`ErrorDetection`](#errordetection) | `ErrorDetection` -> `TotalCostAllocation` | **0.8826** |
| 33 | [`BillHead`](#billhead) | `AmortizeBill_I` -> `BillBasevalue` | **0.8619** |
| 34 | [`PO_ItemCalculation`](#poitemcalculation) | `PO_ItemCalculation` -> `AmountinLocalCurrency` | **0.8148** |
| 35 | [`CostAllocationMaster`](#costallocationmaster) | `CostAllocationMaster` -> `costallocationamount` | **0.8530** |
| 36 | [`POCostAllocation1`](#pocostallocation1) | `POCostAllocation` -> `CostAllocationParameterValue` | **0.8440** |
| 37 | [`TCostAllocationValue`](#tcostallocationvalue) | `TCostAllocationValue` -> `TCostAllocationValue` | **0.8701** |
| 38 | [`POCostAllocation`](#pocostallocation) | `POCostAllocation` -> `CostAllocationParameterValue` | **0.8727** |
| 39 | [`AP`](#ap) | `AP` -> `SNO` | **0.8224** |
| 40 | [`POWF`](#powf) | `POWF` -> `DocumentValue` | **0.8371** |
| 41 | [`IM`](#im) | `BillCostAllocation1` -> `costallocationamount` | **0.7904** |
| 42 | [`VM`](#vm) | `VM` -> `SNO` | **0.8244** |
| 43 | [`G&SRN_BT3H`](#gsrnbt3h) | `G&SRN_BT3I` -> `TotalAcceptedQty` | **0.8925** |
| 44 | [`BT3I`](#bt3i) | `G&SRN_BT3I` -> `AmountinLocalCurrency` | **0.8685** |
| 45 | [`G&SRN_BT3I`](#gsrnbt3i) | `G&SRN_BT3I` -> `TotalAcceptedQty` | **0.8772** |
| 46 | [`CostAllocationMaster`](#costallocationmaster) | `CostAllocationMaster` -> `costallocationamount` | **0.8603** |
| 47 | [`G&SRNCostAllocation1`](#gsrncostallocation1) | `G&SRNCostAllocation` -> `CostAllocationParameterValue` | **0.8138** |
| 48 | [`TCostAllocationValue`](#tcostallocationvalue) | `TCostAllocationValue` -> `TCostAllocationValue` | **0.8844** |
| 49 | [`AD`](#ad) | `AD` -> `CummThresholdLimit` | **0.8217** |
| 50 | [`ExpAcc`](#expacc) | `ExpAcc` -> `Value` | **0.8653** |
| 51 | [`TDSAcc`](#tdsacc) | `TDSAcc` -> `AmountinLocalCurrency2` | **0.8574** |
| 52 | [`Provision`](#provision) | `G&SRN_BT3I` -> `TotalAcceptedQty` | **0.8293** |
| 53 | [`GRIRAc`](#grirac) | `GRIRAc` -> `AmountinTransactionCurrency` | **0.8634** |
| 54 | [`CostProvisionJournal`](#costprovisionjournal) | `ReversalProvisionExpAcc` -> `Value` | **0.8516** |
| 55 | [`G&SRNCostAllocation`](#gsrncostallocation) | `G&SRNCostAllocation` -> `CostAllocationParameterValue` | **0.8683** |
| 56 | [`AP`](#ap) | `AP` -> `SNO` | **0.8234** |
| 57 | [`G&SRNWF`](#gsrnwf) | `G&SRN_BT3I` -> `TotalAcceptedQty` | **0.8560** |

---

## Detailed Schema Reports

### 1. Schema: `ReverseCA`

**Business Purpose:**
> The 'ReverseCA' schema is designed to compute 2 components from data sourced via 'ReverseCAM', settling the process on a Per createdid Monthly basis. It also feeds information into 3 downstream classes.

**Technical Logic:**
> This schema aggregates data using 'ForPrdFrom' as the date aggregation, processed through 'TT'. It includes 7 conditions and is configured to handle 2 components from the 'ReverseCAM' source, ensuring monthly settlement based on 'Per createdid'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8427** | `ReversalProvision` | `TDSValue` | `ReversalProvision_TDSValue_92` | Schema Name: ReversalProvision         Component Name: TDSValue         Compo... |
| 2 | **0.8372** | `ReversalProvision` | `ProvisionValue` | `ReversalProvision_ProvisionValue_91` | Schema Name: ReversalProvision         Component Name: ProvisionValue        ... |
| 3 | **0.8307** | `ReverseCA` | `amountinlocalcurrency` | `ReverseCA_amountinlocalcurrency_0` | Schema Name: ReverseCA         Component Name: amountinlocalcurrency         ... |

---

### 2. Schema: `Bill_I`

**Business Purpose:**
> This schema is designed to compute and aggregate data from the Bill_I source for monthly settlements per lineid, utilizing the TT output process code. It includes 1 component and handles 31 conditions related to the data aggregation.

**Technical Logic:**
> The schema aggregates data from the 'Bill_I' source with a 'ForPrdFrom' date aggregation on, aiming for a 'Per Lineid Monthly' settlement type using the 'TT' output process code. It processes 1 component and manages 31 conditions.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8579** | `BillHead` | `totalrate` | `BillHead_totalrate_216` | Schema Name: BillHead         Component Name: totalrate         Component Typ... |
| 2 | **0.8553** | `Bill_Item` | `TotalQty` | `Bill_Item_TotalQty_37` | Schema Name: Bill_Item         Component Name: TotalQty         Component Typ... |
| 3 | **0.8529** | `PO&IPVsBill` | `Bill` | `PO&IPVsBill_Bill_205` | Schema Name: PO&IPVsBill         Component Name: Bill         Component Type:... |

---

### 3. Schema: `Bill_H`

**Business Purpose:**
> The component 'Bill_H' is designed to compute 3 components from Bill_H data source and settle it on a monthly basis for each interimid. It also feeds the results into 37 downstream classes, performing arithmetic transformations across 25 field conditions.

**Technical Logic:**
> This schema aggregates data based on the 'documentdate', ensuring that computations are performed per interimid at a monthly frequency. The component utilizes the provided fields and conditions to generate outputs for multiple downstream systems.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8719** | `PO&IPVsBill` | `Bill` | `PO&IPVsBill_Bill_205` | Schema Name: PO&IPVsBill         Component Name: Bill         Component Type:... |
| 2 | **0.8660** | `Bill_I` | `invoiceqty` | `Bill_I_invoiceqty_2` | Schema Name: Bill_I         Component Name: invoiceqty         Component Type... |
| 3 | **0.8624** | `Bill_Item` | `DocumentValue` | `Bill_Item_DocumentValue_50` | Schema Name: Bill_Item         Component Name: DocumentValue         Componen... |

---

### 4. Schema: `PrevBill`

**Business Purpose:**
> The 'PrevBill' schema is designed to compute 8 components from the PWBill data source and settle the process on a Per ItemName Monthly basis. It then feeds these computations into 12 downstream classes, performing arithmetic transformations across 21 field conditions.

**Technical Logic:**
> This schema aggregates data using the 'ForPrdFrom' date aggregation method from the 'PWBill' data source. It is configured to handle a settlement type of 'Per ItemName Monthly'. The schema includes 8 components and processes 21 condition fields, all managed through the output process code 'TT'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8536** | `PrevBill` | `Basevalue` | `PrevBill_Basevalue_11` | Schema Name: PrevBill         Component Name: Basevalue         Component Typ... |
| 2 | **0.8410** | `PrevBill` | `DocumentValue` | `PrevBill_DocumentValue_13` | Schema Name: PrevBill         Component Name: DocumentValue         Component... |
| 3 | **0.8377** | `PrevBill` | `AddlCharge` | `PrevBill_AddlCharge_8` | Schema Name: PrevBill         Component Name: AddlCharge         Component Ty... |

---

### 5. Schema: `PO&IP_Status`

**Business Purpose:**
> Error generating text

**Technical Logic:**
> Error generating text

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8302** | `PO&IPVsBill` | `POorIPRate` | `PO&IPVsBill_POorIPRate_176` | Schema Name: PO&IPVsBill         Component Name: POorIPRate         Component... |
| 2 | **0.8178** | `POCostAllocation` | `TCostAllocationValue` | `POCostAllocation_TCostAllocationValue_240` | Schema Name: POCostAllocation         Component Name: TCostAllocationValue   ... |
| 3 | **0.7895** | `PO&IP_Status` | `Basevalue` | `PO&IP_Status_Basevalue_24` | Schema Name: PO&IP_Status         Component Name: Basevalue         Component... |

---

### 6. Schema: `Bill_Item`

**Business Purpose:**
> Error generating text

**Technical Logic:**
> Error generating text

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8720** | `Bill_Item` | `headaddlcharge` | `Bill_Item_headaddlcharge_36` | Schema Name: Bill_Item         Component Name: headaddlcharge         Compone... |
| 2 | **0.8399** | `BillHead` | `totaldocumentvalue` | `BillHead_totaldocumentvalue_218` | Schema Name: BillHead         Component Name: totaldocumentvalue         Comp... |
| 3 | **0.8393** | `BillHead` | `totalbasevalue` | `BillHead_totalbasevalue_215` | Schema Name: BillHead         Component Name: totalbasevalue         Componen... |

---

### 7. Schema: `CostAllocationMaster`

**Business Purpose:**
> Error generating text

**Technical Logic:**
> Error generating text

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8189** | `POCostAllocation` | `TCostAllocationValue` | `POCostAllocation_TCostAllocationValue_240` | Schema Name: POCostAllocation         Component Name: TCostAllocationValue   ... |
| 2 | **0.8179** | `ErrorDetection` | `TotalOrderBaseValue` | `ErrorDetection_TotalOrderBaseValue_209` | Schema Name: ErrorDetection         Component Name: TotalOrderBaseValue      ... |
| 3 | **0.8144** | `BillHead` | `totalbasevalue` | `BillHead_totalbasevalue_215` | Schema Name: BillHead         Component Name: totalbasevalue         Componen... |

---

### 8. Schema: `BillCostAllocation1`

**Business Purpose:**
> This schema is designed to fetch and aggregate data from the Bill_I source for monthly settlements per LOB, aggregating it under the schema name 'BillCostAllocation1'. It includes 2 components and uses a technical process code TT.

**Technical Logic:**
> The schema aggregates data based on the date_aggregation_on field set as 'ForPrdFrom' to perform monthly settlements. It processes data from Bill_I source with a component count of 2, using output_process_code TT for downstream processing.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8740** | `BillCostAllocation` | `AmountinLocalCurrency2` | `BillCostAllocation_AmountinLocalCurrency2_158` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 2 | **0.8471** | `BillCostAllocation1` | `costallocationamount` | `BillCostAllocation1_costallocationamount_66` | Schema Name: BillCostAllocation1         Component Name: costallocationamount... |
| 3 | **0.8468** | `BillCostAllocation` | `AmountinLocalCurrency` | `BillCostAllocation_AmountinLocalCurrency_159` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |

---

### 9. Schema: `TCostAllocationValue`

**Business Purpose:**
> This schema is designed to aggregate three components from data sourced via 'Bill_I' and settle it monthly based on the cost allocation method. It then feeds these aggregated results into three downstream classes.

**Technical Logic:**
> The schema aggregates data from the 'Bill_I' source, groups them according to the specified criteria (likely defined by 'has_getgroupfromschema2'), and processes them using a process code 'TT'. The aggregation is done monthly ('ForPrdFrom') based on the cost allocation method. It includes three conditions that determine how these components are aggregated or processed.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8689** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |
| 2 | **0.8626** | `BillCostAllocation` | `AmountinLocalCurrency2` | `BillCostAllocation_AmountinLocalCurrency2_158` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 3 | **0.8588** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_67` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |

---

### 10. Schema: `AP`

**Business Purpose:**
> This schema is designed to compute three components from the AP data source and settle the process monthly per strategy name. It also feeds 20 downstream classes and performs arithmetic transformations on 43 field conditions.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' and processes it using a specified output code 'TT'. It includes 1 component and 14 conditions, with no getgroupfromschema2 functionality. The technical logic involves aggregating the data source to meet monthly settlement requirements for different strategy names.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8242** | `AP` | `SNO` | `AP_SNO_245` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 2 | **0.8109** | `AP` | `SNO` | `AP_SNO_68` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 3 | **0.8109** | `AP` | `SNO` | `AP_SNO_313` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |

---

### 11. Schema: `BillWF`

**Business Purpose:**
> The 'BillWF' schema is designed to compute 1 components from data sourced via the 'Bill_I' system, specifically for monthly settlements based on LOB (Line of Business) criteria.

**Technical Logic:**
> This schema aggregates data by the 'DocumentDate', processes it through the output process code 'TT', and includes conditions that manage up to 7 different scenarios. It is configured within the 'Bill Process' group and does not utilize a getgroupfromschema2 function.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8631** | `BillWF` | `DocumentValue` | `BillWF_DocumentValue_69` | Schema Name: BillWF         Component Name: DocumentValue         Component T... |
| 2 | **0.8435** | `BillCostAllocation` | `AmountinLocalCurrency2` | `BillCostAllocation_AmountinLocalCurrency2_158` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 3 | **0.8348** | `PO&IPVsBill` | `BillDocumentValue` | `PO&IPVsBill_BillDocumentValue_201` | Schema Name: PO&IPVsBill         Component Name: BillDocumentValue         Co... |

---

### 12. Schema: `AD`

**Business Purpose:**
> This schema is designed to compute 6 components from AD data source and settle per accountcode monthly. It also feeds 69 downstream classes by performing arithmetic transformations across 21 field conditions.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' and processes it using the output process code 'TT'. It has a component count of 3, with each component being settled based on the settlement type 'Per accountcode Monthly'. The technical logic involves applying 21 different field conditions to perform arithmetic transformations.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8274** | `AD` | `CummThresholdLimit` | `AD_CummThresholdLimit_72` | Schema Name: AD         Component Name: CummThresholdLimit         Component ... |
| 2 | **0.8246** | `AD` | `SingleTresholdLimit` | `AD_SingleTresholdLimit_71` | Schema Name: AD         Component Name: SingleTresholdLimit         Component... |
| 3 | **0.8216** | `Bill_Item` | `PAccBaseValue` | `Bill_Item_PAccBaseValue_55` | Schema Name: Bill_Item         Component Name: PAccBaseValue         Componen... |

---

### 13. Schema: `IM`

**Business Purpose:**
> This schema is designed to compute two components from data sourced via the IM system and settle it monthly per item ID. It also feeds 22 downstream classes.

**Technical Logic:**
> The schema 'IM' aggregates data based on a 'ForPrdFrom' date, with a settlement type of 'Per itemid Monthly'. It processes data through 1 component and has 13 conditions. The output is processed using the code 'TT', and it integrates with other systems via downstream classes.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8104** | `IM` | `PercentageofTDS` | `IM_PercentageofTDS_73` | Schema Name: IM         Component Name: PercentageofTDS         Component Typ... |
| 2 | **0.8056** | `BillCostAllocation1` | `costallocationamount` | `BillCostAllocation1_costallocationamount_66` | Schema Name: BillCostAllocation1         Component Name: costallocationamount... |
| 3 | **0.8009** | `IM` | `PercentageofTDS` | `IM_PercentageofTDS_247` | Schema Name: IM         Component Name: PercentageofTDS         Component Typ... |

---

### 14. Schema: `VM`

**Business Purpose:**
> This schema is designed to compute two components from VM data source and settle per member ID monthly. It also feeds 13 downstream classes.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' and processes it using the output process code 'TT'. It includes 15 conditions for conditional processing, has no need for getting group information from schema2, and is intended to handle Per member ID monthly settlements.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8223** | `VM` | `SNO` | `VM_SNO_248` | Schema Name: VM         Component Name: SNO         Component Type: MATH     ... |
| 2 | **0.8174** | `VM` | `SNO` | `VM_SNO_74` | Schema Name: VM         Component Name: SNO         Component Type: MATH     ... |
| 3 | **0.8024** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |

---

### 15. Schema: `ProcessedTDSAmtinGSE`

**Business Purpose:**
> This schema is designed to compute 1 components from VBill data source and settle per senderaccount Monthly. It feeds 9 downstream classes.

**Technical Logic:**
> It aggregates the data based on 'ForPrdFrom' date, processes it through output process code TT, considering 15 conditions and has no need for getgroupfromschema2.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.7903** | `ProcessedTDSAmtinGSE` | `amountinlocalcurrency` | `ProcessedTDSAmtinGSE_amountinlocalcurrency_75` | Schema Name: ProcessedTDSAmtinGSE         Component Name: amountinlocalcurren... |
| 2 | **0.7887** | `PO&IPVsBill` | `DiffDocumentValue` | `PO&IPVsBill_DiffDocumentValue_203` | Schema Name: PO&IPVsBill         Component Name: DiffDocumentValue         Co... |
| 3 | **0.7861** | `PO&IPVsBill` | `DiffDiscountAmt` | `PO&IPVsBill_DiffDiscountAmt_187` | Schema Name: PO&IPVsBill         Component Name: DiffDiscountAmt         Comp... |

---

### 16. Schema: `ReversalTDS`

**Business Purpose:**
> The 'ReversalTDS' schema aggregates and allocates 5 components from the 'Bill_I' data source, settling per ItemID on a monthly basis. It processes arithmetic transformations across 14 field conditions and feeds the results to downstream classes.

**Technical Logic:**
> This schema is designed to aggregate and allocate data based on specific criteria defined by the 'settlement_type'. It uses the provided 'data_source' (Bill_I) for aggregation, with components counted at 'component_count' (5). The logic involves applying conditions from 'condition_count' (14), ensuring arithmetic transformations are applied correctly. The schema is structured to be grouped using 'has_getgroupfromschema2', and it aggregates data on a 'date_aggregation_on' basis ('ForPrdFrom').

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8621** | `ReversalTDS` | `Value` | `ReversalTDS_Value_78` | Schema Name: ReversalTDS         Component Name: Value         Component Type... |
| 2 | **0.8570** | `ReversalProvision` | `TDSValue` | `ReversalProvision_TDSValue_92` | Schema Name: ReversalProvision         Component Name: TDSValue         Compo... |
| 3 | **0.8439** | `ReversalProvisionExpAcc` | `BillValue` | `ReversalProvisionExpAcc_BillValue_84` | Schema Name: ReversalProvisionExpAcc         Component Name: BillValue       ... |

---

### 17. Schema: `ReversalProvisionExpAcc`

**Business Purpose:**
> This schema is designed to aggregate and allocate data from the Bill_I source for the 'ReversalProvisionExpAcc' component. It aggregates 8 components per month based on ItemID and settles according to a Per ItemID Monthly rule, feeding output to five downstream classes.

**Technical Logic:**
> It processes data from the Bill_I source, aggregating it into monthly batches (based on date_aggregation_on 'ForPrdFrom'). The schema is configured for Per ItemID Monthly settlement type with 13 condition fields. It uses a total of 8 components and has no getgroupfromschema2 functionality.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8680** | `ReversalProvisionExpAcc` | `ProvisionValue` | `ReversalProvisionExpAcc_ProvisionValue_83` | Schema Name: ReversalProvisionExpAcc         Component Name: ProvisionValue  ... |
| 2 | **0.8635** | `ReversalProvisionExpAcc` | `BillValue` | `ReversalProvisionExpAcc_BillValue_84` | Schema Name: ReversalProvisionExpAcc         Component Name: BillValue       ... |
| 3 | **0.8588** | `ReversalProvisionExpAcc` | `currentprovisionvalue` | `ReversalProvisionExpAcc_currentprovisionvalue_85` | Schema Name: ReversalProvisionExpAcc         Component Name: currentprovision... |

---

### 18. Schema: `ReversalProvision`

**Business Purpose:**
> The 'ReversalProvision' schema aggregates and allocates 7 components from the 'Bill_I' data source, settling on a monthly basis per ItemID. It performs arithmetic transformations across 14 field conditions to ensure accurate financial calculations.

**Technical Logic:**
> This schema is designed to aggregate and allocate data based on the 'ForPrdFrom' date aggregation rule for the 'SC00002' source schema. It operates under a 'Per ItemID Monthly' settlement type, processing 7 components with 14 condition-based field transformations using output process code 'TT'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8866** | `ReversalProvision` | `ProvisionValue` | `ReversalProvision_ProvisionValue_91` | Schema Name: ReversalProvision         Component Name: ProvisionValue        ... |
| 2 | **0.8845** | `ReversalProvision` | `AmountinTransactionCurrency` | `ReversalProvision_AmountinTransactionCurrency_95` | Schema Name: ReversalProvision         Component Name: AmountinTransactionCur... |
| 3 | **0.8840** | `ReversalProvision` | `TDSValue` | `ReversalProvision_TDSValue_92` | Schema Name: ReversalProvision         Component Name: TDSValue         Compo... |

---

### 19. Schema: `ProvisionReversalAccountingJournal`

**Business Purpose:**
> This schema is designed to compute and consolidate data from a specific source for accounting purposes within the Bill Process group.

**Technical Logic:**
> It aggregates data from the #consolidate# source, processes 1 condition, and outputs components without grouping based on schema. It feeds one downstream class.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8289** | `ProvisionReversalCostAllocation` | `Value` | `ProvisionReversalCostAllocation_Value_150` | Schema Name: ProvisionReversalCostAllocation         Component Name: Value   ... |
| 2 | **0.8231** | `Provision` | `ExchangeRate` | `Provision_ExchangeRate_291` | Schema Name: Provision         Component Name: ExchangeRate         Component... |
| 3 | **0.8137** | `Provision` | `AmountinTransactionCurrency` | `Provision_AmountinTransactionCurrency_297` | Schema Name: Provision         Component Name: AmountinTransactionCurrency   ... |

---

### 20. Schema: `ExpAccBill_I`

**Business Purpose:**
> This schema aggregates and allocates 5 components from the Bill_I data source, settling per ItemID on a monthly basis. It processes arithmetic transformations across 13 field conditions and feeds the results to downstream classes.

**Technical Logic:**
> It is designed for aggregating and allocating data based on specific criteria (ItemID) within a monthly timeframe. The schema uses the provided data source 'Bill_I' and applies various transformations as defined by the condition_count, ensuring accurate settlement according to the Per ItemID Monthly type. It utilizes the output_process_code 'TT' to process these operations.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8709** | `ExpAccBill_I` | `Value` | `ExpAccBill_I_Value_98` | Schema Name: ExpAccBill_I         Component Name: Value         Component Typ... |
| 2 | **0.8676** | `ExpAccBill_I` | `AmountinTransactionCurrency` | `ExpAccBill_I_AmountinTransactionCurrency_100` | Schema Name: ExpAccBill_I         Component Name: AmountinTransactionCurrency... |
| 3 | **0.8630** | `ExpAccBill_I` | `AmountinLocalCurrency` | `ExpAccBill_I_AmountinLocalCurrency_99` | Schema Name: ExpAccBill_I         Component Name: AmountinLocalCurrency      ... |

---

### 21. Schema: `GSTAccBill_I`

**Business Purpose:**
> This schema aggregates and allocates 9 components from the Bill_I data source, settling per ItemID on a monthly basis. It processes arithmetic transformations across 11 field conditions and feeds the results to two downstream classes.

**Technical Logic:**
> It is designed for aggregating and allocating data based on specific criteria (ItemID) within a defined period (monthly). The schema uses the Bill_I data source, applies various transformations as per specified conditions, and outputs the processed data through an output process code 'TT'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.9012** | `GSTAccBill_I` | `AmountinTransactionCurrency` | `GSTAccBill_I_AmountinTransactionCurrency_109` | Schema Name: GSTAccBill_I         Component Name: AmountinTransactionCurrency... |
| 2 | **0.8998** | `GSTAccBill_I` | `AmountinLocalCurrency` | `GSTAccBill_I_AmountinLocalCurrency_108` | Schema Name: GSTAccBill_I         Component Name: AmountinLocalCurrency      ... |
| 3 | **0.8962** | `GSTAccBill_I` | `BillBaseValue` | `GSTAccBill_I_BillBaseValue_104` | Schema Name: GSTAccBill_I         Component Name: BillBaseValue         Compo... |

---

### 22. Schema: `ExpAccBill_I_GST`

**Business Purpose:**
> The schema 'ExpAccBill_I_GST' aggregates and allocates 9 components from the Bill_I data source, settling per ItemID on a monthly basis. It processes arithmetic transformations across 15 field conditions and feeds the results to two downstream classes.

**Technical Logic:**
> This schema is designed to aggregate and allocate data based on specific criteria (ItemID) within the 'Bill_I' data source. It groups components according to the specified settlement type ('Per ItemID Monthly') and applies arithmetic transformations as defined by 15 conditions. The aggregated results are then processed through an output process code 'TT', ensuring that the information is ready for further downstream processing.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8959** | `ExpAccBill_I_GST` | `BillBaseValue` | `ExpAccBill_I_GST_BillBaseValue_113` | Schema Name: ExpAccBill_I_GST         Component Name: BillBaseValue         C... |
| 2 | **0.8767** | `ExpAccBill_I_GST` | `AmountinTransactionCurrency` | `ExpAccBill_I_GST_AmountinTransactionCurrency_118` | Schema Name: ExpAccBill_I_GST         Component Name: AmountinTransactionCurr... |
| 3 | **0.8706** | `AmortizeBill_I` | `ExpValue_GST` | `AmortizeBill_I_ExpValue_GST_162` | Schema Name: AmortizeBill_I         Component Name: ExpValue_GST         Comp... |

---

### 23. Schema: `TDSAccBill_I`

**Business Purpose:**
> This schema aggregates and allocates 11 components derived from the Bill_I data source, settling per section name on a monthly basis. It then feeds these allocations to two downstream classes while performing arithmetic transformations across 15 field conditions.

**Technical Logic:**
> The schema is designed for aggregating and allocating data with specific fields grouped by 'ForPrdFrom' (monthly) from the Bill_I source. It processes 11 components and handles 15 condition-specific operations, all under a monthly settlement type.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8834** | `TDSAccBill_I` | `AmountinLocalCurrency` | `TDSAccBill_I_AmountinLocalCurrency_128` | Schema Name: TDSAccBill_I         Component Name: AmountinLocalCurrency      ... |
| 2 | **0.8821** | `TDSAccBill_I` | `Value` | `TDSAccBill_I_Value_127` | Schema Name: TDSAccBill_I         Component Name: Value         Component Typ... |
| 3 | **0.8771** | `TDSAccBill_I` | `Value1` | `TDSAccBill_I_Value1_124` | Schema Name: TDSAccBill_I         Component Name: Value1         Component Ty... |

---

### 24. Schema: `ExpAccBill_I_TDS`

**Business Purpose:**
> The schema 'ExpAccBill_I_TDS' aggregates and allocates 6 components from the Bill_I data source. It settles Per ItemID Monthly and feeds two downstream classes by performing arithmetic transformations across 14 field conditions.

**Technical Logic:**
> It processes data from the Bill_I source, aggregating it into a schema named 'ExpAccBill_I_TDS'. The aggregation is done based on the date_aggregation_on attribute set to 'ForPrdFrom', and it settles per ItemID monthly. It involves 14 condition_count field conditions for arithmetic transformations. The output process code TT indicates that this data will be processed further or used in downstream processes.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8575** | `ExpAccBill_I_TDS` | `AmountinTransactionCurrency` | `ExpAccBill_I_TDS_AmountinTransactionCurrency_135` | Schema Name: ExpAccBill_I_TDS         Component Name: AmountinTransactionCurr... |
| 2 | **0.8511** | `ExpAccBill_I_TDS` | `Value1` | `ExpAccBill_I_TDS_Value1_132` | Schema Name: ExpAccBill_I_TDS         Component Name: Value1         Componen... |
| 3 | **0.8382** | `ExpAccBill_I_TDS` | `AmountinLocalCurrency` | `ExpAccBill_I_TDS_AmountinLocalCurrency_134` | Schema Name: ExpAccBill_I_TDS         Component Name: AmountinLocalCurrency  ... |

---

### 25. Schema: `RoundOffAcc`

**Business Purpose:**
> This schema is designed to perform arithmetic transformations and fetches data from the 'Bill_I' source for components related to bill processing. It aggregates data on a per-interim basis and outputs it in a monthly format.

**Technical Logic:**
> The schema processes data based on the 'documentdate', aggregating records that match this date. It uses conditions defined by 'condition_count' (8) to perform arithmetic operations across these components, ensuring accurate financial calculations for bill processing.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8723** | `Bill_H` | `RoundOffValue` | `Bill_H_RoundOffValue_5` | Schema Name: Bill_H         Component Name: RoundOffValue         Component T... |
| 2 | **0.8715** | `RoundOffAcc` | `AmountinTransactionCurrency` | `RoundOffAcc_AmountinTransactionCurrency_138` | Schema Name: RoundOffAcc         Component Name: AmountinTransactionCurrency ... |
| 3 | **0.8560** | `RoundOffAcc` | `AmountinLocalCurrency` | `RoundOffAcc_AmountinLocalCurrency_137` | Schema Name: RoundOffAcc         Component Name: AmountinLocalCurrency       ... |

---

### 26. Schema: `CrAccBill_I`

**Business Purpose:**
> This schema aggregates and allocates 10 components from the Bill_I data source, settling per document number on a monthly basis. It performs arithmetic transformations across 13 field conditions to ensure accurate financial calculations.

**Technical Logic:**
> The schema is designed for aggregating and allocating data based on the 'ForPrdFrom' date aggregation rule. It processes data through the 'TT' output process code, handling up to 10 components with 13 condition fields, ensuring monthly settlement of Per Documentnumber transactions.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8779** | `CrAccBill_I` | `AmountinLocalCurrency` | `CrAccBill_I_AmountinLocalCurrency_147` | Schema Name: CrAccBill_I         Component Name: AmountinLocalCurrency       ... |
| 2 | **0.8683** | `CrAccBill_I` | `AmountinTransactionCurrency` | `CrAccBill_I_AmountinTransactionCurrency_148` | Schema Name: CrAccBill_I         Component Name: AmountinTransactionCurrency ... |
| 3 | **0.8561** | `CrAccBill_I` | `journalsno` | `CrAccBill_I_journalsno_139` | Schema Name: CrAccBill_I         Component Name: journalsno         Component... |

---

### 27. Schema: `AccountingJournal`

**Business Purpose:**
> This schema is designed to compute and consolidate data from a specific source for further processing and distribution.

**Technical Logic:**
> The schema 'AccountingJournal' aggregates data from the '#consolidate#' source, with one condition applied. It does not perform date aggregation but has 0 components based on the provided information.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8119** | `ErrorDetection` | `TotalBillBaseValue` | `ErrorDetection_TotalBillBaseValue_208` | Schema Name: ErrorDetection         Component Name: TotalBillBaseValue       ... |
| 2 | **0.8002** | `Bill_Item` | `AccountBaseValue` | `Bill_Item_AccountBaseValue_53` | Schema Name: Bill_Item         Component Name: AccountBaseValue         Compo... |
| 3 | **0.7986** | `BillCostAllocation` | `BillAmountinLocalCurrency` | `BillCostAllocation_BillAmountinLocalCurrency_156` | Schema Name: BillCostAllocation         Component Name: BillAmountinLocalCurr... |

---

### 28. Schema: `ProvisionReversalCostAllocation`

**Business Purpose:**
> This schema is designed to aggregate and allocate cost data from the Bill_I source system. It groups the data by LOB (Line of Business) monthly and processes four components according to specified conditions, ensuring accurate settlement for downstream systems.

**Technical Logic:**
> The schema aggregates data using 'ForPrdFrom' as the date aggregation criterion, targeting a Per LOB Monthly settlement type. It processes 9 field conditions with arithmetic transformations and includes 4 components from the Bill_I source system.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8664** | `BillCostAllocation` | `AmountinLocalCurrency2` | `BillCostAllocation_AmountinLocalCurrency2_158` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 2 | **0.8635** | `ProvisionReversalCostAllocation` | `Value` | `ProvisionReversalCostAllocation_Value_150` | Schema Name: ProvisionReversalCostAllocation         Component Name: Value   ... |
| 3 | **0.8477** | `BillCostAllocation` | `AmountinLocalCurrency1` | `BillCostAllocation_AmountinLocalCurrency1_157` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |

---

### 29. Schema: `BillCostAllocation`

**Business Purpose:**
> The schema 'BillCostAllocation' aggregates and allocates 7 components from the Bill_I data source. It settles Per LOB Monthly and feeds into downstream classes, performing arithmetic transformations across 10 field conditions.

**Technical Logic:**
> This schema is designed to aggregate and allocate financial costs for different billing categories (components) based on monthly settlements per business line of operation (LOB). It processes data from the Bill_I source, applying various transformations as defined by the condition_count fields.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8931** | `BillCostAllocation` | `AmountinLocalCurrency2` | `BillCostAllocation_AmountinLocalCurrency2_158` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 2 | **0.8778** | `BillCostAllocation` | `AmountinLocalCurrency1` | `BillCostAllocation_AmountinLocalCurrency1_157` | Schema Name: BillCostAllocation         Component Name: AmountinLocalCurrency... |
| 3 | **0.8631** | `PO&IPVsBill` | `Bill` | `PO&IPVsBill_Bill_205` | Schema Name: PO&IPVsBill         Component Name: Bill         Component Type:... |

---

### 30. Schema: `AmortizeBill_I`

**Business Purpose:**
> This schema is designed to aggregate and allocate 12 components derived from the Bill_I data source. It settles the data on a Per Itemid Monthly basis and performs arithmetic transformations across 13 field conditions, ensuring accurate financial calculations.

**Technical Logic:**
> The schema aggregates data based on 'ForPrdFrom' date aggregation logic and processes it according to the 'Per Itemid Monthly' settlement type. It involves 12 components and handles 13 condition fields through an output process code of 'TT', with no need for a getgroupfromschema2 operation.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8956** | `AmortizeBill_I` | `BillBasevalue` | `AmortizeBill_I_BillBasevalue_165` | Schema Name: AmortizeBill_I         Component Name: BillBasevalue         Com... |
| 2 | **0.8729** | `AmortizeBill_I` | `Basevalue` | `AmortizeBill_I_Basevalue_169` | Schema Name: AmortizeBill_I         Component Name: Basevalue         Compone... |
| 3 | **0.8683** | `AmortizeBill_I` | `DiscountAmt` | `AmortizeBill_I_DiscountAmt_167` | Schema Name: AmortizeBill_I         Component Name: DiscountAmt         Compo... |

---

### 31. Schema: `PO&IPVsBill`

**Business Purpose:**
> This schema aggregates financial data from the PO&IPVsBillRep source to provide monthly settlements per source, performing necessary transformations on 36 components.

**Technical Logic:**
> It processes data from the specified data source, aggregating and settling it according to the 'Per Source Monthly' type. It applies conditions for arithmetic operations across 2 fields.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8834** | `PO&IPVsBill` | `Different` | `PO&IPVsBill_Different_207` | Schema Name: PO&IPVsBill         Component Name: Different         Component ... |
| 2 | **0.8803** | `PO&IPVsBill` | `BillQty` | `PO&IPVsBill_BillQty_173` | Schema Name: PO&IPVsBill         Component Name: BillQty         Component Ty... |
| 3 | **0.8795** | `PO&IPVsBill` | `DiffDocumentValue` | `PO&IPVsBill_DiffDocumentValue_203` | Schema Name: PO&IPVsBill         Component Name: DiffDocumentValue         Co... |

---

### 32. Schema: `ErrorDetection`

**Business Purpose:**
> The schema 'ErrorDetection' aggregates 7 components from the Bill_I data source and settles per documentnumber on a monthly basis. It performs arithmetic transformations across 9 field conditions.

**Technical Logic:**
> This schema is designed to process and aggregate data from the Bill_I source, focusing on aggregating 7 components with specific field conditions settled according to 'Per documentnumber Monthly' logic.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8826** | `ErrorDetection` | `TotalCostAllocation` | `ErrorDetection_TotalCostAllocation_210` | Schema Name: ErrorDetection         Component Name: TotalCostAllocation      ... |
| 2 | **0.8632** | `ErrorDetection` | `TotalBillBaseValue` | `ErrorDetection_TotalBillBaseValue_208` | Schema Name: ErrorDetection         Component Name: TotalBillBaseValue       ... |
| 3 | **0.8544** | `ErrorDetection` | `CostAllocationVariance` | `ErrorDetection_CostAllocationVariance_211` | Schema Name: ErrorDetection         Component Name: CostAllocationVariance   ... |

---

### 33. Schema: `BillHead`

**Business Purpose:**
> This schema aggregates financial data from the Bill_H source, aggregating 7 components and settling per interimid on a monthly basis. It performs arithmetic transformations across 17 field conditions to ensure accurate financial calculations.

**Technical Logic:**
> It processes data from the 'Bill_H' source with a documentdate for aggregation, applying 17 condition-based transformations to calculate financial values in groups defined by 'intermid'. The output is processed using code TT and includes 7 components.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8619** | `AmortizeBill_I` | `BillBasevalue` | `AmortizeBill_I_BillBasevalue_165` | Schema Name: AmortizeBill_I         Component Name: BillBasevalue         Com... |
| 2 | **0.8596** | `BillHead` | `amountintransactioncurrency` | `BillHead_amountintransactioncurrency_220` | Schema Name: BillHead         Component Name: amountintransactioncurrency    ... |
| 3 | **0.8556** | `BillHead` | `totalrate` | `BillHead_totalrate_216` | Schema Name: BillHead         Component Name: totalrate         Component Typ... |

---

### 34. Schema: `PO_ItemCalculation`

**Business Purpose:**
> The schema 'PO_ItemCalculation' is designed to compute 13 components from data sourced via 'PO_I'. It aggregates the data on a per-lineid monthly basis and outputs it through an output process code of 'TT', settling the computations accordingly. This ensures that downstream classes receive accurate, aggregated information for further processing.

**Technical Logic:**
> This schema processes data from the 'PO_I' source to compute 13 components with 21 field conditions. It aggregates this data on a per-lineid monthly basis and outputs it using the specified output process code 'TT'. The aggregation is done based on the date_aggregation_on setting of 'ForPrdFrom', ensuring that the computations are performed correctly according to the provided settings.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8148** | `PO_ItemCalculation` | `AmountinLocalCurrency` | `PO_ItemCalculation_AmountinLocalCurrency_232` | Schema Name: PO_ItemCalculation         Component Name: AmountinLocalCurrency... |
| 2 | **0.8095** | `PO_ItemCalculation` | `AmountinTransactionCurrency` | `PO_ItemCalculation_AmountinTransactionCurrency_233` | Schema Name: PO_ItemCalculation         Component Name: AmountinTransactionCu... |
| 3 | **0.8081** | `PO_ItemCalculation` | `Rate` | `PO_ItemCalculation_Rate_224` | Schema Name: PO_ItemCalculation         Component Name: Rate         Componen... |

---

### 35. Schema: `CostAllocationMaster`

**Business Purpose:**
> The 'CostAllocationMaster' schema is designed to compute 10 components from the CA data source and settle per LOB monthly. It also feeds into 19 downstream classes by performing arithmetic transformations across 24 field conditions.

**Technical Logic:**
> This schema aggregates data using a 'ForPrdFrom' date aggregation, processes it with a 'Per LOB Monthly' settlement type, and operates based on 8 condition counts from the CA data source. It utilizes 3 components to achieve its purpose.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8530** | `CostAllocationMaster` | `costallocationamount` | `CostAllocationMaster_costallocationamount_64` | Schema Name: CostAllocationMaster         Component Name: costallocationamoun... |
| 2 | **0.8417** | `CostAllocationMaster` | `PERC_CostAllocationValue` | `CostAllocationMaster_PERC_CostAllocationValue_236` | Schema Name: CostAllocationMaster         Component Name: PERC_CostAllocation... |
| 3 | **0.8378** | `CostAllocationMaster` | `CNT_CostAllocationValue` | `CostAllocationMaster_CNT_CostAllocationValue_266` | Schema Name: CostAllocationMaster         Component Name: CNT_CostAllocationV... |

---

### 36. Schema: `POCostAllocation1`

**Business Purpose:**
> This schema is designed to fetch and process data from the PO_I source for cost allocation purposes. It aggregates data 'ForPrdFrom' and settles it monthly per LOB (Line of Business), ensuring that 1 component is fetched and fed into 4 downstream classes.

**Technical Logic:**
> The schema named 'POCostAllocation1' retrieves information from the 'SC00004' source, specifically designed for PO_I data. It aggregates this data based on a date range specified as 'ForPrdFrom'. The settlement type is set to 'Per LOB Monthly', meaning it processes and distributes the fetched components according to different Line of Business monthly. This schema includes 5 conditions and has no need to fetch groups from the schema directly ('has_getgroupfromschema2' is False).

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8440** | `POCostAllocation` | `CostAllocationParameterValue` | `POCostAllocation_CostAllocationParameterValue_241` | Schema Name: POCostAllocation         Component Name: CostAllocationParameter... |
| 2 | **0.8384** | `POCostAllocation` | `POAmountinLocalCurrency` | `POCostAllocation_POAmountinLocalCurrency_243` | Schema Name: POCostAllocation         Component Name: POAmountinLocalCurrency... |
| 3 | **0.8342** | `POCostAllocation1` | `CostAllocationParameterValue` | `POCostAllocation1_CostAllocationParameterValue_238` | Schema Name: POCostAllocation1         Component Name: CostAllocationParamete... |

---

### 37. Schema: `TCostAllocationValue`

**Business Purpose:**
> This schema is designed to aggregate three components from PO_I data source and settle per CostAllocationMethod Monthly. It then feeds the aggregated data into three downstream classes.

**Technical Logic:**
> The schema aggregates 3 components from the PO_I data source, applies a monthly settlement based on the Per CostAllocationMethod type, and processes this information through 1 component with 3 conditions.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8701** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |
| 2 | **0.8547** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_239` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |
| 3 | **0.8479** | `POCostAllocation` | `CostAllocationParameterValue` | `POCostAllocation_CostAllocationParameterValue_241` | Schema Name: POCostAllocation         Component Name: CostAllocationParameter... |

---

### 38. Schema: `POCostAllocation`

**Business Purpose:**
> This schema is designed to aggregate and allocate cost data from the PO_I source system into a structured format for monthly settlement per LOB (Line of Business). It processes 5 components with arithmetic transformations applied based on 6 conditions, ensuring accurate financial allocations.

**Technical Logic:**
> The schema aggregates data from the 'PO_I' source system under the 'SC00004' source schema within the 'PO Validation' group. It groups and allocates costs according to the specified settlement type of 'Per LOB Monthly'. The process involves 5 components with arithmetic operations applied based on 6 conditions defined in the schema.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8727** | `POCostAllocation` | `CostAllocationParameterValue` | `POCostAllocation_CostAllocationParameterValue_241` | Schema Name: POCostAllocation         Component Name: CostAllocationParameter... |
| 2 | **0.8714** | `POCostAllocation` | `POAmountinLocalCurrency` | `POCostAllocation_POAmountinLocalCurrency_243` | Schema Name: POCostAllocation         Component Name: POAmountinLocalCurrency... |
| 3 | **0.8518** | `POCostAllocation` | `AmountinLocalCurrency` | `POCostAllocation_AmountinLocalCurrency_244` | Schema Name: POCostAllocation         Component Name: AmountinLocalCurrency  ... |

---

### 39. Schema: `AP`

**Business Purpose:**
> This schema is designed to compute three components from the AP data source and settle monthly per strategy name. It integrates 20 downstream classes and applies arithmetic transformations across 43 field conditions.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' and processes it using a settlement type of 'Per StrategyName Monthly'. It includes 1 output process code (TT) with 14 condition counts, ensuring that the data is transformed according to specific criteria defined in the schema.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8224** | `AP` | `SNO` | `AP_SNO_245` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 2 | **0.8108** | `AP` | `SNO` | `AP_SNO_68` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 3 | **0.8108** | `AP` | `SNO` | `AP_SNO_313` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |

---

### 40. Schema: `POWF`

**Business Purpose:**
> This schema is designed to compute 1 components from PO_I data source and settle per LOB monthly.

**Technical Logic:**
> It aggregates the 'DocumentDate' for processing and uses a Per LOB Monthly settlement type with 3 conditions, without requiring a getgroupfromschema2 operation.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8371** | `POWF` | `DocumentValue` | `POWF_DocumentValue_246` | Schema Name: POWF         Component Name: DocumentValue         Component Typ... |
| 2 | **0.8022** | `BillWF` | `DocumentValue` | `BillWF_DocumentValue_69` | Schema Name: BillWF         Component Name: DocumentValue         Component T... |
| 3 | **0.8014** | `PO&IPVsBill` | `DiffBasevalue` | `PO&IPVsBill_DiffBasevalue_195` | Schema Name: PO&IPVsBill         Component Name: DiffBasevalue         Compon... |

---

### 41. Schema: `IM`

**Business Purpose:**
> This schema is designed to compute two components from data sourced via the IM system. It aggregates data based on a period specified by 'ForPrdFrom' and settles it monthly per itemid. The output feeds into 22 downstream systems.

**Technical Logic:**
> The schema processes data from the IM source, aggregating it according to the 'date_aggregation_on' field set as 'ForPrdFrom'. It includes 13 conditions for processing and outputs two components which are then settled monthly per itemid. The results are distributed to 22 downstream systems.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.7904** | `BillCostAllocation1` | `costallocationamount` | `BillCostAllocation1_costallocationamount_66` | Schema Name: BillCostAllocation1         Component Name: costallocationamount... |
| 2 | **0.7866** | `IM` | `PercentageofTDS` | `IM_PercentageofTDS_73` | Schema Name: IM         Component Name: PercentageofTDS         Component Typ... |
| 3 | **0.7820** | `ErrorDetection` | `TotalCostAllocation` | `ErrorDetection_TotalCostAllocation_210` | Schema Name: ErrorDetection         Component Name: TotalCostAllocation      ... |

---

### 42. Schema: `VM`

**Business Purpose:**
> This schema is designed to compute two components from VM data source and settle per member ID on a monthly basis, feeding the results into 13 downstream classes.

**Technical Logic:**
> The schema aggregates data based on 'ForPrdFrom' date aggregation. It processes data through Per memberid Monthly settlement type and utilizes 12 conditions for conditional processing. The schema is configured to have one component and does not require getting group from schema 2.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8244** | `VM` | `SNO` | `VM_SNO_248` | Schema Name: VM         Component Name: SNO         Component Type: MATH     ... |
| 2 | **0.8188** | `VM` | `SNO` | `VM_SNO_74` | Schema Name: VM         Component Name: SNO         Component Type: MATH     ... |
| 3 | **0.8127** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |

---

### 43. Schema: `G&SRN_BT3H`

**Business Purpose:**
> This schema is designed to compute 1 components from the G&SRNBT3H data source and settle it monthly per SenderAccount. It also feeds into 3 downstream classes.

**Technical Logic:**
> It aggregates data based on the Accountingdate, using Per SenderAccount Monthly settlement type, processes with output_process_code TT, and includes 23 conditions. The schema is grouped under 'Cost_Provision_BasedOnGRN&SRN'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8925** | `G&SRN_BT3I` | `TotalAcceptedQty` | `G&SRN_BT3I_TotalAcceptedQty_254` | Schema Name: G&SRN_BT3I         Component Name: TotalAcceptedQty         Comp... |
| 2 | **0.8871** | `G&SRN_BT3I` | `AmountinLocalCurrency` | `G&SRN_BT3I_AmountinLocalCurrency_261` | Schema Name: G&SRN_BT3I         Component Name: AmountinLocalCurrency        ... |
| 3 | **0.8803** | `G&SRN_BT3I` | `AmountinTransactionCurrency` | `G&SRN_BT3I_AmountinTransactionCurrency_262` | Schema Name: G&SRN_BT3I         Component Name: AmountinTransactionCurrency  ... |

---

### 44. Schema: `BT3I`

**Business Purpose:**
> This schema is designed to compute 3 components from the G&SRNBT3I data source and settle it on a monthly basis for each item description. It also feeds information to 15 downstream classes, performing arithmetic transformations based on 21 field conditions.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' (likely meaning per period from) into components using the G&SRNBT3I source and applies a monthly settlement type. It processes these components through 21 different condition fields to ensure accurate computations, ultimately feeding results to multiple downstream systems.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8685** | `G&SRN_BT3I` | `AmountinLocalCurrency` | `G&SRN_BT3I_AmountinLocalCurrency_261` | Schema Name: G&SRN_BT3I         Component Name: AmountinLocalCurrency        ... |
| 2 | **0.8668** | `G&SRN_BT3I` | `BaseValue` | `G&SRN_BT3I_BaseValue_258` | Schema Name: G&SRN_BT3I         Component Name: BaseValue         Component T... |
| 3 | **0.8648** | `G&SRN_BT3I` | `AmountinTransactionCurrency` | `G&SRN_BT3I_AmountinTransactionCurrency_262` | Schema Name: G&SRN_BT3I         Component Name: AmountinTransactionCurrency  ... |

---

### 45. Schema: `G&SRN_BT3I`

**Business Purpose:**
> This schema is designed to aggregate 13 components from the G&SRNBT3I data source and settle the data on a Per itemdescription Monthly basis. It also processes arithmetic transformations across 21 field conditions, feeding the results into 8 downstream classes.

**Technical Logic:**
> The schema aggregates data with a component count of 13, sourced from the 'G&SRNBT3I' data source and aggregated based on 'ForPrdFrom'. It settles the data monthly per item description. The technical logic involves applying arithmetic transformations to 21 field conditions.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8772** | `G&SRN_BT3I` | `TotalAcceptedQty` | `G&SRN_BT3I_TotalAcceptedQty_254` | Schema Name: G&SRN_BT3I         Component Name: TotalAcceptedQty         Comp... |
| 2 | **0.8763** | `G&SRN_BT3I` | `AmountinLocalCurrency` | `G&SRN_BT3I_AmountinLocalCurrency_261` | Schema Name: G&SRN_BT3I         Component Name: AmountinLocalCurrency        ... |
| 3 | **0.8752** | `G&SRN_BT3I` | `AmountinTransactionCurrency` | `G&SRN_BT3I_AmountinTransactionCurrency_262` | Schema Name: G&SRN_BT3I         Component Name: AmountinTransactionCurrency  ... |

---

### 46. Schema: `CostAllocationMaster`

**Business Purpose:**
> The 'CostAllocationMaster' schema is designed to compute 10 components from the CA data source and settle per LOB monthly. It also feeds into 19 downstream classes and performs arithmetic transformations across 24 field conditions.

**Technical Logic:**
> This schema aggregates data based on a 'ForPrdFrom' date, processes it through the 'TT' output process code, and is grouped by LOB for monthly settlements. It involves 3 components and has 8 conditions that are applied to perform arithmetic operations.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8603** | `CostAllocationMaster` | `costallocationamount` | `CostAllocationMaster_costallocationamount_64` | Schema Name: CostAllocationMaster         Component Name: costallocationamoun... |
| 2 | **0.8478** | `CostAllocationMaster` | `PERC_CostAllocationValue` | `CostAllocationMaster_PERC_CostAllocationValue_236` | Schema Name: CostAllocationMaster         Component Name: PERC_CostAllocation... |
| 3 | **0.8461** | `CostAllocationMaster` | `CNT_CostAllocationValue` | `CostAllocationMaster_CNT_CostAllocationValue_266` | Schema Name: CostAllocationMaster         Component Name: CNT_CostAllocationV... |

---

### 47. Schema: `G&SRNCostAllocation1`

**Business Purpose:**
> This schema is designed to fetch and process data from the G&SRNBT3I source for monthly settlements based on different LOBs. It aggregates data 'ForPrdFrom' and processes 1 component, ensuring that the information is distributed to 4 downstream systems.

**Technical Logic:**
> The schema is configured to retrieve data from the specified source ('G&SRNBT3I') and aggregate it according to a predefined date field ('ForPrdFrom'). It includes conditions for processing and outputs the relevant components to four different processes ('TT').

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8138** | `G&SRNCostAllocation` | `CostAllocationParameterValue` | `G&SRNCostAllocation_CostAllocationParameterValue_307` | Schema Name: G&SRNCostAllocation         Component Name: CostAllocationParame... |
| 2 | **0.8125** | `G&SRNCostAllocation` | `TCostAllocationValue` | `G&SRNCostAllocation_TCostAllocationValue_306` | Schema Name: G&SRNCostAllocation         Component Name: TCostAllocationValue... |
| 3 | **0.8049** | `G&SRNCostAllocation1` | `CostAllocationParameterValue` | `G&SRNCostAllocation1_CostAllocationParameterValue_269` | Schema Name: G&SRNCostAllocation1         Component Name: CostAllocationParam... |

---

### 48. Schema: `TCostAllocationValue`

**Business Purpose:**
> The row/component is designed to aggregate data from the G&SRNBT3I source for CostAllocationValue schema. It settles monthly based on the cost allocation method and processes 1 component with 6 conditions, feeding the results into 3 downstream classes.

**Technical Logic:**
> This row represents a process that aggregates data from the specified source (G&SRNBT3I) under the 'Cost_Provision_BasedOnGRN&SRN' schema group. It is configured to aggregate monthly and includes processing for one component with six conditions, ultimately feeding its output into three downstream processes.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8844** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |
| 2 | **0.8654** | `G&SRNCostAllocation` | `TCostAllocationValue` | `G&SRNCostAllocation_TCostAllocationValue_306` | Schema Name: G&SRNCostAllocation         Component Name: TCostAllocationValue... |
| 3 | **0.8576** | `G&SRNCostAllocation` | `CostAllocationParameterValue` | `G&SRNCostAllocation_CostAllocationParameterValue_307` | Schema Name: G&SRNCostAllocation         Component Name: CostAllocationParame... |

---

### 49. Schema: `AD`

**Business Purpose:**
> This schema is designed to compute 6 components using data from the AD source. It settles monthly per account code and feeds information to 69 downstream systems. The system performs arithmetic transformations based on 21 field conditions.

**Technical Logic:**
> The schema aggregates data 'ForPrdFrom' and processes it according to Per accountcode Monthly settlement type, utilizing a total of 3 components with 21 conditional operations.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8217** | `AD` | `CummThresholdLimit` | `AD_CummThresholdLimit_72` | Schema Name: AD         Component Name: CummThresholdLimit         Component ... |
| 2 | **0.8204** | `AD` | `SingleTresholdLimit` | `AD_SingleTresholdLimit_71` | Schema Name: AD         Component Name: SingleTresholdLimit         Component... |
| 3 | **0.8176** | `AD` | `SingleTresholdLimit` | `AD_SingleTresholdLimit_272` | Schema Name: AD         Component Name: SingleTresholdLimit         Component... |

---

### 50. Schema: `ExpAcc`

**Business Purpose:**
> This schema aggregates data from the G&SRNBT3I source to calculate costs based on GRNs and SRNs per item ID on a monthly basis. It processes 7 components and settles the output in Per ItemID Monthly format, feeding results to six downstream systems.

**Technical Logic:**
> It uses the SC00026 schema group from G&SRNBT3I data source to aggregate cost-related information for each item ID across multiple GRNs and SRNs. The aggregation is performed monthly and involves 19 conditional transformations on the component count of 7.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8653** | `ExpAcc` | `Value` | `ExpAcc_Value_276` | Schema Name: ExpAcc         Component Name: Value         Component Type: SUM... |
| 2 | **0.8482** | `ExpAccBill_I_GST` | `BillBaseValue` | `ExpAccBill_I_GST_BillBaseValue_113` | Schema Name: ExpAccBill_I_GST         Component Name: BillBaseValue         C... |
| 3 | **0.8463** | `ExpAcc` | `AmountinLocalCurrency1` | `ExpAcc_AmountinLocalCurrency1_277` | Schema Name: ExpAcc         Component Name: AmountinLocalCurrency1         Co... |

---

### 51. Schema: `TDSAcc`

**Business Purpose:**
> This schema aggregates financial data from G&SRNBT3I for cost provisioning based on GRNs and SRNs, settling the aggregation per section name monthly. It processes 9 components and applies arithmetic transformations to 19 field conditions before feeding the results into two downstream systems.

**Technical Logic:**
> The schema 'TDSAcc' aggregates data from the source schema 'SC00026', which is a G&SRNBT3I dataset, for cost provisioning. It groups by section names and performs monthly settlements. The aggregation process involves 9 components and includes arithmetic operations on 19 conditions defined in the schema.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8574** | `TDSAcc` | `AmountinLocalCurrency2` | `TDSAcc_AmountinLocalCurrency2_287` | Schema Name: TDSAcc         Component Name: AmountinLocalCurrency2         Co... |
| 2 | **0.8539** | `TDSAcc` | `AmountinLocalCurrency` | `TDSAcc_AmountinLocalCurrency_288` | Schema Name: TDSAcc         Component Name: AmountinLocalCurrency         Com... |
| 3 | **0.8530** | `TDSAcc` | `Value` | `TDSAcc_Value_285` | Schema Name: TDSAcc         Component Name: Value         Component Type: MAT... |

---

### 52. Schema: `Provision`

**Business Purpose:**
> This schema is designed to aggregate 8 components from the G&SRNBT3I data source and settle the data on a per-item basis monthly. It performs arithmetic transformations across 18 field conditions.

**Technical Logic:**
> It aggregates data based on 'ForPrdFrom' date aggregation, using the provided schema name 'Provision', with a settlement type of 'Per ItemID Monthly'. The process code is 'TT' and it involves 8 components from the specified source. It also includes 18 condition counts for field transformations.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8293** | `G&SRN_BT3I` | `TotalAcceptedQty` | `G&SRN_BT3I_TotalAcceptedQty_254` | Schema Name: G&SRN_BT3I         Component Name: TotalAcceptedQty         Comp... |
| 2 | **0.8266** | `ProvisionReversalCostAllocation` | `Value` | `ProvisionReversalCostAllocation_Value_150` | Schema Name: ProvisionReversalCostAllocation         Component Name: Value   ... |
| 3 | **0.8247** | `Provision` | `AmountinTransactionCurrency` | `Provision_AmountinTransactionCurrency_297` | Schema Name: Provision         Component Name: AmountinTransactionCurrency   ... |

---

### 53. Schema: `GRIRAc`

**Business Purpose:**
> This schema is designed to fetch and aggregate data from the G&SRNBT3I source for cost provisioning based on GRN & SRN. It settles the data per ItemID monthly and performs necessary arithmetic transformations as defined in 18 conditions.

**Technical Logic:**
> The schema 'GRIRAc' aggregates data from the 'G&SRNBT3I' source, grouping by 'ForPrdFrom'. It processes a total of 8 components with 18 condition-driven field transformations to achieve cost-based provisioning per ItemID on a monthly basis.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8634** | `GRIRAc` | `AmountinTransactionCurrency` | `GRIRAc_AmountinTransactionCurrency_305` | Schema Name: GRIRAc         Component Name: AmountinTransactionCurrency      ... |
| 2 | **0.8615** | `GRIRAc` | `ExchangeRate` | `GRIRAc_ExchangeRate_299` | Schema Name: GRIRAc         Component Name: ExchangeRate         Component Ty... |
| 3 | **0.8520** | `GRIRAc` | `AmountinLocalCurrency1` | `GRIRAc_AmountinLocalCurrency1_302` | Schema Name: GRIRAc         Component Name: AmountinLocalCurrency1         Co... |

---

### 54. Schema: `CostProvisionJournal`

**Business Purpose:**
> This row describes a data schema named 'CostProvisionJournal' that aggregates data from the '#consolidate#' source. It is designed to compute one condition and does not settle any values.

**Technical Logic:**
> The schema 'CostProvisionJournal' uses the '#consolidate#' data source, has 1 condition but no aggregation on date or settlement type specified. It will process 0 components.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8516** | `ReversalProvisionExpAcc` | `Value` | `ReversalProvisionExpAcc_Value_86` | Schema Name: ReversalProvisionExpAcc         Component Name: Value         Co... |
| 2 | **0.8490** | `TCostAllocationValue` | `TCostAllocationValue` | `TCostAllocationValue_TCostAllocationValue_270` | Schema Name: TCostAllocationValue         Component Name: TCostAllocationValu... |
| 3 | **0.8417** | `ErrorDetection` | `TotalBillBaseValue` | `ErrorDetection_TotalBillBaseValue_208` | Schema Name: ErrorDetection         Component Name: TotalBillBaseValue       ... |

---

### 55. Schema: `G&SRNCostAllocation`

**Business Purpose:**
> This schema is designed to aggregate and allocate cost data from the G&SRNBT3I source for each LOB on a monthly basis. It performs arithmetic transformations across 13 field conditions and outputs the results in a TT process.

**Technical Logic:**
> The schema aggregates data based on 'ForPrdFrom' date aggregation, processes it through Per LOB Monthly settlement type, and applies 13 condition-specific operations using the provided source schema SC00026. It includes 7 components and is grouped according to the getgroupfromschema2 field.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8683** | `G&SRNCostAllocation` | `CostAllocationParameterValue` | `G&SRNCostAllocation_CostAllocationParameterValue_307` | Schema Name: G&SRNCostAllocation         Component Name: CostAllocationParame... |
| 2 | **0.8525** | `G&SRNCostAllocation` | `TCostAllocationValue` | `G&SRNCostAllocation_TCostAllocationValue_306` | Schema Name: G&SRNCostAllocation         Component Name: TCostAllocationValue... |
| 3 | **0.8485** | `G&SRN_BT3I` | `TotalAcceptedQty` | `G&SRN_BT3I_TotalAcceptedQty_254` | Schema Name: G&SRN_BT3I         Component Name: TotalAcceptedQty         Comp... |

---

### 56. Schema: `AP`

**Business Purpose:**
> This schema is designed to compute three components from the AP data source and settle them monthly per strategy name. It also feeds 20 downstream classes and performs arithmetic transformations across 43 field conditions.

**Technical Logic:**
> The schema aggregates data based on 'ForPrdFrom' date, processes it using a Per StrategyName Monthly settlement type, and includes 15 condition counts for conditional operations. It utilizes the output process code TT to manage the aggregation and downstream integration.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8234** | `AP` | `SNO` | `AP_SNO_245` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 2 | **0.8100** | `AP` | `SNO` | `AP_SNO_68` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |
| 3 | **0.8100** | `AP` | `SNO` | `AP_SNO_313` | Schema Name: AP         Component Name: SNO         Component Type: MATH     ... |

---

### 57. Schema: `G&SRNWF`

**Business Purpose:**
> This schema is designed to compute 1 components from the G&SRNBT3H data source and settle monthly based on the sender account.

**Technical Logic:**
> The schema 'G&SRNWF' aggregates data from the 'SC00026' source, with a date aggregation set to 'Accountingdate'. It uses the 'data_source' 'G&SRNBT3H', has 12 conditions and outputs using process code 'TT'. The settlement type is specified as 'Per senderaccount Monthly'.

#### Top Component Matches:
| Rank | Cosine Similarity | Target Schema | Target Component | Database ID | Text Snippet |
|---|---|---|---|---|---|
| 1 | **0.8560** | `G&SRN_BT3I` | `TotalAcceptedQty` | `G&SRN_BT3I_TotalAcceptedQty_254` | Schema Name: G&SRN_BT3I         Component Name: TotalAcceptedQty         Comp... |
| 2 | **0.8379** | `G&SRN_BT3I` | `AmountinTransactionCurrency` | `G&SRN_BT3I_AmountinTransactionCurrency_262` | Schema Name: G&SRN_BT3I         Component Name: AmountinTransactionCurrency  ... |
| 3 | **0.8361** | `G&SRNCostAllocation` | `AmountinLocalCurrency` | `G&SRNCostAllocation_AmountinLocalCurrency_312` | Schema Name: G&SRNCostAllocation         Component Name: AmountinLocalCurrenc... |

---