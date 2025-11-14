| case | Absent ≤ 20% | CC > 0 | GK > 0 | CK ≥ 4 | TB ≥ 4.0 | No Violation | Expected Result | Reason (if Fail) |
|-------|---------------|--------|--------|--------|-----------|----------------|------------------|------------------|
| Case 1 | Yes | Yes | Yes | Yes | Yes | Yes | Pass | — |
| Case 2 | No | Yes | Yes | Yes | Yes | Yes | Fail | Too many absences |
| Case 3 | Yes | No | Yes | Yes | Yes | Yes | Fail | CC =< 0 |
| Case 4 | Yes | Yes | No | Yes | Yes | Yes | Fail | GK = 0 |
| Case 5 | Yes | Yes | Yes | No | Yes | Yes | Fail | CK < 4 |
| Case 6 | Yes | Yes | Yes | Yes | No | Yes | Fail | TB < 4.0 |
| Case 7 | Yes | Yes | Yes | Yes | Yes | No | Fail | Violated exam rules |
| Case 8 | No | No | No | No | No | No | Fail | All conditions failed |
| R9 |      |      |      |      |      |      |      |      |       |


| TC ID    | AS | MS | FS  | Vio       | FG Calculation                                                      | Expected Result   | Covered Branches                  |                   |                        |
| -------- | -- | -- | --- | --------- | ------------------------------------------------------------------- | ----------------- | --------------------------------- | ----------------- | ---------------------- |
| **TC01** | 5  | 5  | 5   | **true**  | FG ignored                                                          | **Fail**          | Vio=true branch                   |                   |                        |
| **TC02** | 8  | 7  | 9   | **false** | FG = 0.1*8 + 0.3*7 + 0.6*9 = 8.2 ≥ 5                                | **Passed**        | Vio=false, FG≥5, FS≥4, MS>0, AS>0 |                   |                        |
| **TC03** | 2  | 2  | 1   | **false** | FG = 0.1*2 + 0.3*2 + 0.6*1 = 1.4 < 5                                | **Fail**          | Vio=false, FG<5                   |                   |                        |
| **TC04** | 3  | 3  | 3.5 | **false** | FG = 0.1*3 + 0.3*3 + 0.6*3.5 = 3.3 <5 → check FS                    | FS < 4 → check MS | MS>0 → check AS                   | AS>0 → **Passed** | FG<5, FS<4, MS>0, AS>0 |
| **TC05** | 0  | 5  | 5   | **false** | FG = 0.1*0 + 0.3*5 + 0.6*5 = 4.5 <5 → FS≥4 → MS>0 → AS≤0 → **Fail** | FG<5, FS≥4, AS≤0  |                                   |                   |                        |
| **TC06** | 2  | 0  | 3   | **false** | FG = 0.1*2 +0.3*0 +0.6*3 = 2.0 <5 → FS<4 → MS≤0 → **Fail**          | FG<5, FS<4, MS≤0  |                                   |                   |                        |

