from Common_Files.Case_handler import CaseDoc 

case = CaseDoc()
case.judgement_text = """ Appeal made by the defendant. The appellants in these appeals and special leave petitions are Suba Singh (A-1) and his son Shingara Singh (A-2). They were both tried by the Additional Sessions Judge, Sirsa in Sessions Trial No.46 of 1991 charged variously of offences under Sections 302, 307, 302/34, 307/34 IPC and under Section 25/27 of the Arms Act. The learned Additional Sessions Judge by his judgment and order dated March 6, 1992 acquitted A-2 of all the charges levelled against him but found A-1 guilty of the offence under Section 304 Part I holding that he had exceeded his right of private defence. Accordingly, he sentenced A-1 to undergo rigorous imprisonment for a period of 10 years and to pay a fine of Rs.50,000/-, in default further to undergo rigorous imprisonment for a period of two years. Both the appellants were acquitted of other charges levelled against them.


Aggrieved by the judgment and order of the learned Additional Sessions Judge, Criminal Appeal No. 375-DBA of 1992 was preferred by the State of Haryana before the High Court of Punjab and Haryana at Chandigarh against the acquittal of A-2 under Sections 302 and 307 read with Section 34 IPC. Suba Singh preferred Criminal Appeal No. 105-SB of 1992 against his conviction under Section 304 Part I IPC, while the informant Balbir Singh preferred a Criminal Revision No.68 of 1993 against the same impugned judgment and order acquitting the appellants of the other charges levelled against them. The two Appeals and the Criminal Revision have been disposed of by a common judgment and order of the High Court dated March 6, 1992. The High Court allowed the appeal filed by the State and held A-2 guilty of the offence under sections 302 and 307 IPC. A-1 was found guilty and convicted under Section 302/34 and 307/34 IPC. A-1 was also found guilty of the offence under Section 27 of the Arms Act. A-2 has been sentenced to undergo life imprisonment under Section 302 IPC and to pay a fine of Rs.10,000/- and in default to undergo further rigorous imprisonment for two years. He has also been sentenced to undergo rigorous imprisonment for 10 years under Section 307 IPC and to pay a fine of Rs.5,000/- in default to undergo further rigorous imprisonment for one year. A-1 has been sentenced to undergo life imprisonment under Section 302/34 IPC and to pay a fine of Rs.10,000/- in default to undergo further rigorous imprisonment for ten years. Under Section 307/34 IPC he has been sentenced to undergo rigorous imprisonment for ten years and to pay a fine of Rs.5,000/- in default to undergo further rigorous imprisonment for one year. While so allowing the appeal preferred by the State the High Court has in a mechanical manner allowed the Criminal Revision preferred by the informant, which in effect had become infructuous since an appeal had been preferred by the State which was ultimately allowed. In any event a Criminal Revision preferred by a private party against an order of acquittal could not result in the conviction of the accused.


"""

case.process_text()
print(case.case_id)