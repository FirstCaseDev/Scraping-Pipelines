import re
import spacy

nlp = spacy.load('en_core_web_sm')

month = "((January)|(JAN)|(February)|(FEB)|(March)|(MAR)|(April)|(apr)|(May)|(June)|(Jun)|(July)|(jul)|(August)|(Aug)|(September)|(Sept)|(October)|(OCT)|(November)|(NOVEMBER)|(NOV)|(Nov)|(nov)|(December)|(DEC))"
text= """08-02-2001.
PETITIONER:

TATA CELLULAR

Vs.

RESPONDENT:

UNION OF INDIA

DATE OF JUDGMENT

BENCH:

MOHAN, S. (J)

BENCH:

MOHAN, S. (J)

VENKATACHALLIAH, M.N.(CJ)

PUNCHHI, M.M.


The Judgement of the Court was delivered by MOHAN ,J.-- Leave granted.

2.All these appeals can be dealt with under a common judgment since one and same issue requires to be decided. The brief facts are as under.

3.The Department of Telecommunications, Government of India, invited tenders from Indian Companies with a view to license the operation of "Cellular Mobile Telephone Service" in four metropolitan cities of India, namely, Delhi, Bombay, Calcutta and Madras. Cellular mobile telephone means a telecommunication system which allows two-ways tele- communication between a mobile or stationary telephone to another mobile or stationary unit at a location. It may be within or outside the city including subscriber-cum-dialling and international subscriber-cum-dialling calls. The last date for submission of tender was 31-3-1992. The tender process was in two stages. First stage involved technical evaluation and the second involved financial evaluation. Those who were short-listed at the first stage were invited for the second stage.

4.Thirty bidders participated initially at the first stage. The first Tender Evaluation Committee was constituted consisting of senior officers of the Department of Telecommunications.

5.A Telecom Commission was constituted on 6-4-1989 comprising a Chairman and four full-time Members:

1. Member (Production)

2. Member (Services)

3. Member (Technology)

4. Member (Finance) It short-listed 16 companies, 12 of which were eligible without any defect. However, in the case of 4 the Committee recommended condonation of certain defects. Those four were :

1. BPL Systems and Projects Limited

2. Mobile Telecommunication Limited

3. Mobile Telecom Services

4. Indian Telecom Limited Between 19-5-1992 and 27-5-1992 the recommendations were submitted to the Telecom Commission. The matter came up for discussion among the members of the Commission. On 27-5- 1992 the Telecom Commission accepted the recommendations of the Technical Evaluation Committee. The Chairman recommended that the short-list of bidders, the recommendations of the Tender Evaluation Committee and the proposal for financial bids be placed before the Selection Committee at the earliest.

6.It requires to be noted, at this stage, that a Selection Committee also described as Apex/High-Powered Committee comprising the Principal Secretary to the Prime Minister and three other Secretaries to the Government of India had been set up by the Minister for final evaluation of the bid.

7.Mr B.R. Nair, a Member (Budget) of Telecom Commission came to be appointed as Member (Services) on 29-5-1992. It appears the Selection Committee met a number of times and discussed the matter with the Minister. He submitted an interim report on 16-7-1992. During this time the Committee not only de novo exercised but also modified the short-list prepared by the Technical Evaluation Committee and approved 14 companies. The Selection Committee also met the representatives of equipment manufacturers for the selection of the licensees. On 20-7-1992, the revised financial bid and the short-list approved by the Telecom Commission were put up before the Minister for approval. On 24-7-1992, further meetings of the Selection Committee were held and the financial bid document was revised. On 28-7-1992, the Selection Committee submitted its final report. Two bidders, namely, M/s Ashok Leyland Ltd. and M/s Vam Organics Ltd. were dropped from the short-list of 16 bidders. On 29- 7-1992, Mr Nair was appointed as Director General of Telecommunications. He was authorised to exercise all powers of Telecom Authority under Section 3 of the Telegraph Act. The Minister approved the issue of financial bids with modification to the short-listed companies as recommended by the Selection Committee on 29-7-1992. The approval took place on 30-7-1992.

8.On 30-7-1992, the financial tenders were issued. It contained seven criteria which had been approved by the Selection Committee. However, no marks were earmarked for any of the criteria. 17-8-1992 was the cut-off date for financial bid document. On this date the bids received from 14 companies were opened and read out to the bidders, who were present. As per the conditions, the quoted rental ceilings and the cities for which the bids were made, were read out.

9.Another Departmental Tender Evaluation Committee consisting of senior officers examined the financial bids of the 14 short-listed companies. It adopted some parameter and devised the marking system which was not done by the Selection Committee. On 2-9-1992, the second Tender Evaluation Committee submitted its recommendations. However, the matter was referred back to it for a fresh gradation on the basis of 21.75 per cent interest rate in respect of 13 per cent rate which it had earlier adopted. On 7-9-1992 the recommendations were re-submitte. The Adviser operations recommended only 4 operators based on the evaluation and financial bids. Bharati Cellular was recommended as a first choice for all the four cities, BPL as the second choice for both Delhi and Bombay, Tata Cellular and Skycell as second choice for Calcutta and Madras. This was done since in his view no other bidder qualified for licence. On 10-9-1992 the Chairman of the Tender Evaluation Committee directed that all the documents and recommendations be sent to the Selection Committee for its consideration and for making final recommendations to the Government. When the file was put up to the Minister on 9-10-1992 he made three important notings :

1. In view of the time taken by the High- Powered Committee the selection process be completed by DoT internally;

2. Only one party may be granted licence for one city; and

3. The actual selection of the licensee should be made primarily on the consideration of rentals and the marks obtained in respect of foreign exchange inflow and outflow criterion and experience of the licensee.

10. On 9-10-1992, in accordance with this note, a list of 8 short-listed companies was prepared. The reasons for rejection of the 6 companies were recorded. The Chairman, in his final recommendation, made on 9-10-1992, noted that Bharati Cellular, Modi Telecom and Mobile Telecom did not fulfil the conditions provided in clause 2.4.7 of Chapter 11 of the financial bid which requires that foreign exchange requirement be met by foreign collaborator. With regard to rejection of 6 bidders Sterling Cellular was rejected because some investigation against them was pending before the CBI. However, the Minister reversed that decision as to the exclusion of Sterling Cellular and Indian Telecom Limited from the list of finally approved bidders and directed that the same be considered.

11.On 10-10-1992, the list was recast. Sterling Cellular was provisionally selected for the city of Madras. On 12-10-1992, the selected bidders were notified of their provisional selection subject to the acceptance of rentals and other terms as might be advised.

12.It is under these circumstances, four writ petitions were preferred bearing CWP Nos. 4030, 4031, 4032 and 163 of 1992. The petitioners were

1. India Telecomp (Petitioner in CWP No. 4030 of 1992)

2. Adino Telecom Limited (Petitioner in CWP No. 4031 of 1992)

3. Kanazia Digital System (Petitioner in CWP No. 4032 of 1992)

4. Hutchison Max Telecom Private Limited (Petitioner in CWP No. 163 of 1992)

13.It was urged before the High Court of Delhi that the decision of the Government in selecting 8 parties, two for each of the cities, was bad on the following grounds-

(i) bias

(ii)invoking certain hidden criteria

(iii)irrelevant considerations

(iv)bypassing the Selection Committee

(v) selecting otherwise underqualified parties

(vi)marketing system which was evaluated by the second Technical Evaluation Committee for grading various bidders.

14.So manipulated thereby a criterion was evolved which was tailormade to knock out the petitioners before the High Court or resulting in knocking out of the petitioner in the case of India Telecomp Limited and Adino Telecom Limited. Hutchison Max Telecom Private Limited urged that it was the highest in the gradation. Its bid was not considered for a technical and flimsy reason; in that, the compliance statement required to be furnished with the bids was not complete. Kanazia Digital System contended that its technical bid was left out on certain wrong premise.

15.Lengthy arguments were advanced before the High Court. On a consideration of those arguments the writ petitions of Adino Telecom and Kanazia Digital System were dismissed. CYR No. 4030 of 1992 filed by India Telecomp was allowed. A mandamus was issued to consider afresh the grant of licence to the petitioner therein, after evaluating marks for the rental on the basis the figures of deposits from subscribers given for Delhi and Bombay were accumulated. Similarly, CWP No. 163 of 1992 in which the petitioner was M/s Hutchison Max Telecom Private Limited, was allowed. A direction was issued to reconsider the case of the petitioner, on the basis the compliance filed by it, as it was in order. To that extent the order granting licence to 8 parties (2 for each of the cities) was set aside. This judgment was pronounced on 26-2-1993.

16.After the judgment of the Delhi High Court, the matter was reconsidered in the light of the said judgment. A revised list of provisionally selected bidders was prepared on 27-8-1993. That is as follows :

Position as on 12-10-1992Position as on 27-8-1993 Bombay Bombay Bharati Cellular Hutchison Max BPL Projects & Systems Bharati Cellular Delhi Delhi India Telecomp Ltd. BPL Projects & Systems Tata Cellular Pvt. Ltd. Sterling Cellular Ltd.

It could be seen from the above that TataCellular which was originally selected for Delhi has been left out.

Therefore, it has preferred SLP (Civil) Nos. 14191-94 of 1993. M/s Hutchison Max Private Limited has apprehended that if the judgment of the Delhi High Court is not accepted it is likely to be displaced from the provisional selection list for Delhi. Indian Telecom Private Limited preferred SLP (C) No. 17809 of 1993. India Telecomp preferred SLP (C) No. 14266 of 1993.

17. Mr Soli J. Sorabjee, learned counsel for the appellant, Tata Cellular, argues that this is a two-staged tender. In the first stage, the evaluation had to be made on the basis of technical and commercial considerations. The bidders short-listed at the first stage would then compete in the second stage, namely, the financial bid. Chapter 11 contains general conditions framed into the bid. In paragraph 2.4.7 the financial projection of the proposed cellular mobile service was prescribed. The notes mentioned three criteria :

(i) Entire foreign exchange requirement shall be met by the foreign collaborator.

(ii) Minimum reliance on Indian public financial institutions will be preferred.

(iii) Debt equity ratio should not be more than 2 : 1.

18. It is borne out by records that out of the seven criteria in evaluating the financial bid, six parameters alone were taken into consideration. For rental parameter the evaluation committee took into account the equity rental ceiling, security deposits installation and other charges indicated in the bid which were the same in the case of all the bidders. This was done in order to arrive at an equated or effective figure of monthly rental for each bidder. It is not open to the Committee to totally ignore this criterion when the Chairman's note dated 9-10-1992 specifically states that the companies would be asked to comply with the conditions of financial bid in clause 2.4.7 of Chapter II while granting licences. When this is the position, strangely, the appellant is informed as follows :

"Ministry of Communication (Telecom Commission) New Delhi - 11 000 1 No. /92-TM Dated: 27-8-1993 To, (Kind attention Subject:Tender No. 44-21/9 1 -MMC (FIN) for franchise for Cellular Mobile Telephone Service for Bombay, Delhi, Calcutta and Madras.

Sir, Kindly refer letter of even No. dated 12-10- 1992 informing you that you have been provisionally selected for franchise for providing cellular mobile telephone service at .... on a nonexclusive basis.

2. The matter has been reconsidered in the light of the judgment delivered by the High Court of Delhi in this case. M/s .......... have now been provisionally selected for franchise for providing cellular mobile telephone service at in place of ........... on a non-exclusive basis. The other franchise selected for is M/s with M/s of.......as their foreign partner.3. The details of the rental, deposits and other terms fixed for the franchise will be intimated to you shortly.

4.Kindly get necessary formalities completed by 30-9-1993. Yours faithfully, (S.K. Garg) DDG (TM)"

19. The second ground of attack is bias. In that, Mr B.R. Nair, Member of Production in the Telecom Commission, who was appointed as Member (Service) on 29-5-1992, participated. From the Adviser the file went to Member (Service). The note of Mr Nair is dated 21-5-1992. He agreed with the recommendation of TEC that four firms which had some deficiencies should be included in the short-list. They were BPL Systems and Projects, Mobile Telecom, Mobile Communications and Indian Cellular. Therefore, BPL was approved by Mr Nair. Admittedly, Mr Nair's son is employed in BPL Systems and Projects.

20. The High Court in dealing with the allegations of bias made against Mr Nair held: "Nexus of father and son in the chain of decision-making process is too remote to be of any consequence. It is quite interesting to note that of the four companies which were having some deficiencies in their tender documents in the first stage and were recommended for consideration by the first TEC, three companies including BPL made it to the final list of eight. Plea of bias is not alleged in the selection of other two companies. In the circumstances it is not possible for us to hold any allegation of bias made against Nair."

The High Court concluded:

"We do not think in a case like this the mere fact that Nair was part of the machinery to make selection was enough to show that there could be reasonable suspicion or real likelihood of bias in favour of BPL."

This finding is wrong. Mr Nair's participation from the beginning would constitute bias. In support of this submission, the learned counsel relies on Manak Lal v. Prem Chand1 (and particularly the passage occurring at SCR p.587), J. Mohapatra & Co. v. State of Orissa2 (SCR at p. 334: SCC p. 112) and Ashok Kumar Yadav v. State of Haryana3 (SCC paragraph 16 at p. 440 and 441). The English decision on this aspect which will support the contention is: Metropolitan Properties Co. (EG. C.) Ltd. v. Lannon4.

21. In law, there is no degree of bias. Even otherwise in the implementation of the judgment of the High Court of Delhi, if this appellant is to be eliminated, it ought to have been afforded an opportunity. Had that been done it would have pointed out several factors, namely, the omission to consider relevant material, namely, parameter seven, the prejudice caused by the award of marks after the bids were opened. The DoT was obliged to disclose the maximum marks for each criterion at the threshold of the 1 1957 SCR 575: AIR 1957 SC 425 2 (1984) 4 SCC 103, 112: (1985) 1 SCR 322 3 (1985) 4 SCC 417: 1986 SCC (L&S) 88 4 (1968) 3 All ER 304, 310: (1969) 1 QB 577: (1968) 3 WLR financial bid in the interest of transparency and to ensure a non-arbitrary selection.

22.In the case of most of the bidders the foreign exchange is not met by the foreign collaborator. In the case of India Telecomp the debt equity ratio is 1 : 1. Their total project cost is stated to be Rs 101 crones. This means Rs 50.50 crores represent equity and the other Rs 50.50 crores represent external commercial borrowing. In this case, the entire foreign exchange is not met by the foreign collaborator. Therefore, there is a breach of the fundamental condition of the bid. This would constitute a disqualification which is a bar at the threshold. Had this condition been strictly applied Bharati Cellular, Modi Telecom, Mobile Communications, Hutchison Max, Skycell Communication would have been eliminated. Likewise, Sterling Cellular also did not fulfil this condition.

23.It was a mandatory condition that a foreign collaborator indicated at the first stage-of tender, could not be changed thereafter. Inter alia on the strength of credentials of foreign collaborators the bid is considered. If a change is allowed it would amount to technical violation of the bid. Yet in the case of BPL one of its foreign collaborators, namely, McCaw Cellular withdrew from the collaboration. In spite of this, the breach was disregarded. The bidder had to famish proof that he had obtained the approval of foreign collaboration or filed application before the competent authority. BPL had not even filed an application before the competent authority yet its tender was considered and approved. On the very same ground, while Ashok Leyland had been disqualified, equally it should have been applied to BPL.

24. Sterling Cellular had been rejected at various stages of consideration on the ground that there was criminal complaint/investigation pending against it. The Minister had also agreed but reversed that decision on the last day and directed its consideration for inclusion in Madras on the purported ground that Madras was the least popular of the stations and that if any delay is caused due to complications on account of CBI investigation would have the least adverse effect for lack of competition. The High Court noted that no material had been brought on record to show that there was any complaint against Sterling Cellular. But, factually, to the knowledge of the DoT, a criminal case stood registered against Sterling Cellular in June 1993, before making the final selection. The DoT, instead of rejecting Sterling Cellular on that ground, upgraded it from Madras to Delhi in disregard of the decision of the Minister.

25. Any foreign collaboration has to be approved by an inter-ministerial committee called FIPB. No proposal for foreign collaboration could be evaluated by the TEC without receiving the approval from the FIPB. Even under the tender documents the bidders were required to show that they had applied for such approval.

26. Having regard to all these, the selection is vitiated by arbitrariness or unfairness.

27. Mr Harish Salve, learned counsel, appearing for India Telecomp attacks the selection as arbitrary on the following three grounds :

1. Bypassing the Apex Committee and entrusting to a Committee which did not follow the norms.

2. Certain hidden criteria which were not disclosed earlier, were applied not as parameters, but for elimination.

3. There are five glaring errors in the selection. One such error is in the case of Sterling Cellular. It supports its bid on the strength of the foreign exchange that may be obtained from foreign tourists. This is something incomprehensible.

Elaborating these points it is urged that after short- listing, the selection committee did not select at all. The counter-affidavit filed on behalf of the Government of India does not mention that there was a delay by Apex Committee, as held by the High Court. On the contrary, the facts disclose there was no delay whatever.

28. Two hidden criteria were postulated. (i) Persons having less than one lakh experience will not be considered. (ii) If two bidders have the same collaborator in relation to foreign exchange that bid will not be considered. These criteria were evolved after 18-8-1992. When one looks at the conditions of tender, paragraph 2.2.1 talks of subscriber's capacity. That does not mention about the nature of experience. Equally, paragraph 2.4.5 makes no mention about one foreign collaborator for each bidder. In the case of Bharati Cellular it was having only eighty-one thousand lines. The criterion of 80 thousand GSM was prescribed only to favour Bharati Cellular.

29. If no change of foreign collaborator is allowed at the stage of financial assessment after the technical committee has passed its bid, in the case to permit such a change to BPL, is clearly arbitrary.

30. Indian Telecom was excluded because it has the same foreign collaborator, namely, Telecom Malaysia. However, in the case of Bharati Cellular, that test was not applied. Its collaborator is Talkland Vodaphone. The same Vodaphone has been the collaborator with Mobile Telecom. This would amount to adopting double standards.

31. As against BPL the attack is as under:

1. BPL did not apply to SIA/FIPB but to Reserve Bank of India (RBI).

2. The foreign collaborator was changed in the middle, as submitted above, inasmuch as McCaw Cellular withdrew. The joint venture is gone when McCaw was given up.

3. Mr Nair was biased in favour of BPL.

4. Total marks awarded are five. The idea is indigenous equipment whereas what has been done by BPL is to quote higher customs duty.

32. Insofar as Sterling Cellular is preferred for Delhi that again is arbitrary. There is a CBI inquiry pending against it. Secondly, the foreign exchange is sought to be procured by international roaming and it is awarded 10 marks out of 10.

33. Mr Ashoke Sen, learned counsel, appearing for the Indian Telecom submits, firstly, the limits of judicial review in the matter of this kind will have to be examined. Such limits could be gathered from Sterling Computers Ltd. v. M & N Publications Ltd.5 and Union of India v. Hindustan Development Corpn.6 which lay down the methods of reaching conclusion.

34. Generally speaking, in entering into contracts, the public authority is not like a private person. The question to be asked is, have the guidelines been laid down, if so laid down, have they been observed? In this case, Indian Telecom was originally allotted Delhi. By reason of reconsideration pursuant to the judgment of the High Court of Delhi, it has now been allotted Calcutta. This is wrong.

35. In clause 7 of the General Conditions it is stipulated that there can be no change of foreign collaborator. In clause 13, a certificate requires to be produced. In a number of cases no such certificate has been produced. Paragraph 2.4.5 of Chapter 11 of General Conditions lays down one of the parameters is the experience of foreign operating partner. In the case of Bharati Cellular, SFR France Company has no experience. Talkland's sole function is service. Therefore, its experience should not have been added. In paragraph 1.4 the nature of services is listed. These are not the services offered by Talkland. Hutchison Max did not produce any certificate likewise Bharati Cellular.

36. The argument on behalf of Ashok Leyland, petitioner in Transferred Case No. 49 of 1993 is that it was an eligible bidder but has never been communicated the reason as to why it came to be rejected. On 29-9-1992, the Committee records that reasons must be given. Yet no reasons are furnished to the petitioner. Even though the Tender Evaluation Committee held the petitioner to be qualified yet its bid had been rejected without communicating any reason whatever. In Mahabir Auto Stores v. Indian Oil Corpn.7 (SCC at p. 763, paragraph 18) this Court has held that there is an obligation to communicate the reasons.

37. Mr Koura, learned counsel appearing for Bharati Cellular, in opposing the arguments advanced on behalf of the appellants, submits that service operation should not be read in a narrow sense. In telephone industry there could be operation as well as service. While defining the service, relying on paragraph 2.1 is wrong because services are defined in paragraph 1.4 whereas paragraph 21 refers only to obligations of licensee. Besides, the services are also essential, they should be regarded as a part of operation.

38. Mr G. Ramaswamy, learned counsel, appearing for Skycell states that his client has been awarded Madras city. It is submitted that in the absence of mala fides the individual marking system should not have been 5 (1993) 1 SCC 445 6 (1993) 3 SCC 499 7 (1990) 3 SCC 752 interfered with as far as foreign exchange is concerned. In the case of his client regarding the foreign exchange sourcing, inflow is more than the out flow.

39. Mr Anil B. Divan, learned counsel appearing for Mobile Telecom Services submits that though this respondent supports the judgment of the High Court, insofar as it is allowed the writ petition filed by Hutchison Max, the same ought to be reconsidered. The bid of Hutchison Max was rejected since it had filed an incomplete compliance report. The High Court has chosen to accept the bid of Hutchison Max on four grounds :

1. The approach of the Department was hyper-technical.

2. Compliance statement is akin to verification in a pleading. It cannot be placed on a higher pedestal than verification.

3. The Department ought to have allowed rectification since it was purely a mistake unintentionally made.

4. Inasmuch as the Department had allowed a favourable treatment in the case of Indian Telecom Private Limited and Tata Cellular the same treatment ought to have been accorded to Hutchison Max as well.

These findings are attacked on the following grounds. The tender documents both technical and commercial bid as well as the financial bid clearly lay down the manner of compliance. Clause 3 of the technical bid states, in the event of the compliance report not being enclosed with the offer, the offer shall not be considered. Equally, in relation to financial bid, Chapter I states that any offer received after the due date and time shall be rejected. The various other clauses also postulate a strict compliance. If, therefore, the bid is incomplete the offer ought to have been rejected. Hence, there is no question of the Department of Telecommunication condoning the defect. If the view of the High Court is to prevail it would amount to allowing a post tender modification on a select basis, that is, on the basis whether the mistake was intentional or unintentional. Where the Department has chosen to reject, the High Court cannot sit in judgment. To state it is like verification of pleading is to overlook that the pleadings are governed by the verification. That is not the case here. The comparison with Indian Telecom and Tata Cellular is also incorrect. In the case of Indian Telecom there is an unconditional compliance. Only in the covering letter a view has been expressed about the economic viability of the services and the bidders' preference. Hence, it cannot be contended that the bid was conditional, in any manner. Similarly, Tata Cellular was not accompanied in this regard.

40. The allegation against this respondent that the foreign exchange requirement has not been met is incorrect. The documents filed by the respondent clearly show that there is a surplus of approximately three crore rupees, available from the foreign collaborator, in the first year. The allegation of India Telecomp that the bidder was responding on the basis of one party per city and the proposal for licence for a period of 20 to 25 years is factually incorrect. Equally, to state that this respondent quoted a lower customs duty and thereby got higher marks is incorrect. The financial bid of the respondent shows that this had taken customs duty at 95 per cent for the first year when the backlog of the equipment is to be imported. For the subsequent years, the projection was made on a reduced customs duty in view of the announced policy of the Government to reduce customs duty and to bring them in line with international levels.

41. The argument that there is a common collaborator of Bharati Cellular and Mobile Telecom Services proceeds on the footing that Bharati Cellular is collaborating with Talkland. That Talkland has a service privately in agreement with Vodaphone Group. Thus, Vodaphone is the common foreign collaborator of Bharati Cellular and Mobile Telecom. This is not correct. Mobile Telecom has its foreign partner for the purpose of setting up a leading cellular network cooperator of U.K., namely, Vodaphone. Vodaphone as network operator is the owner of Vodaphone Cellular Network. It is responsible for the setting up of the network in U.K. where cellular network operator can also be a service provider. Vodaphone has been issued a licence as the cellular network operator under Section 7 of the U.K. Telecommunications Act of 1984. It is known as a public telecommunication operator. Vodaphone has about 30 service providers in U.K. including Talkland. It has no equity in Talkland. There are no common directors on the boards of two companies. Vodaphone is the foreign collaborator of Mobile Telecom. It has no collaboration agreement with Bharati Cellular. In regard to Bharati Cellular it has only a collaboration agreement with Talkland which is a mere service provider.

42. Arguing on behalf of Sterling Cellular Mr K. Parasaran, learned counsel submits that the technical competency and capacity to execute the contract by this respondent with its joint venture partner is not in doubt. Sterling Cellular was short-listed by Technical Evaluation Committee itself. It was amongst the 12 tenderer short-listed in the first list. The joint venture collaborator of Sterling, namely, Cellular Communication is a reputed international company having large-scale operation in U.S.A. As regards the foreign exchange inflow and outflow it is submitted that Sterling Cellular has projected its stand that the foreign exchange inflow will be from foreign tourists and business travelers visiting the city of Delhi. The expression "international roaming" has been used in relation to such foreign tourists and business travellers. Internationally, cellular phones are used by two categories of persons, (1) subscribers residing in the city who would use the phone on a permanent basis, (2) the tourists and business travellers visiting the city who would use the phone on a temporary basis. Inasmuch as the foreign tourists and foreign business travellers make the payment in foreign currency it will be a source of foreign exchange. What is required under the tender condition is the projection of foreign exchange inflow and outflow relating to the cellular phone contract. This means inflow in foreign exchange as a result of the operation of cellular phone system. Hence, the bearing from tourists and business travellers is a very relevant consideration. Like this respondent, Hutchison Max selected for the Bombay city also projected for the foreign exchange openings by the use of cellular phone by tourists and business travellers. The argument that the foreign tourists and business travellers are not likely to use cellular telephone is not correct since the calls made through the cellular telephones are not only cheaper but also available as a 24 hours' companion. That, of course, is a greater facility. In the note made by the Minister it has been mentioned that the respondent has undertaken to be bound by conditions contained in the tender documents to the effect that the entire foreign exchange requirement shall be met by the foreign collaborator. In fact, the foreign collaborator has also confirmed this.

43. As regards the allegation of CBI inquiry, it is submitted that the learned Judges of the High Court perused the note of the Chairman, Telecom Commission. It was only after this the Court held that there were no strictures against holding company of SCL by the name Sterling Computers Limited, in M&N Publication Ltd. v. MTNL8. It was further held that it appears to have been punished for no sin of it. There was no CBI inquiry on the date of the above judgment. It was after the judgment dated 10-7-1993, the FIR was filed which has been allowed to be proceeded with by way of directions in petition under Section 482 of the Criminal Procedure Code. This Court in Erusian Equipment & Chemicals Ltd. v. State of WB.9 has laid down that pending investigation blacklisting cannot be permitted. The said 1 ratio will apply to this case.

44. Mr K.K. Venugopal, learned counsel appearing for Hutchison Max submits that this respondent was rejected by the committee. That was questioned in the writ petition. The High Court directed reconsideration of its bid. With regard to compliance statement it was stated that the company agrees to fully comply with all paragraphs of Chapter II of the General Conditions and Chapter V : Tariffs of Document No. 44-21/91-MMC(FIN) without any deviation and reservation. No doubt, there is a failure, in the first instance, to state about compliance with Chapters 11 and IV This is an accidental omission. It amounts to a clerical error as laid down in Moffett, Hodgkins & Clarke Co. v. City of Rochester10. If it is a mistake in relation to non- essential or collateral matter it could always be condoned. The Privy Council in Mohd. Ejaz Husain v. Mohd. Iftikhar Husain11 has held that it is always a matter of form and not of substance. Other argument is advanced that there is a defect in the compliance statement.

45. The alternate submission is, the question of error does not arise since the compliance statement was filed on 11-9- 1992 while the contract came to be awarded only on 12-10- 1992. In such a case the question would be what is the scope of judicial review? The court could interfere in the following three categories of cases

1. Quasi-judicial 8 (1992) 4 DLT 24 9 (1975) 1 SCC 70: (1975) 2 SCR 674 10 44 L Ed 373 : 178 US 1108 (1899) 11 AIR 1932 PC 76: 59 IA 92: ILR 7 Luck 1

2. Administrative, for example, price fixing

3. Award of contracts Here, the matter is technical in relation to award of contract. Judicial review does not mean the court should take over the contracting powers. The parameters for interference in such matters would be

(i) Mala fide

(ii) Bias

(iii) Arbitrariness to the extent of perversity. If none of these is present, the court should not interfere. It must be left to the authorities. The contrary arguments advanced on behalf of the appellants against this respondent are not tenable.

46. Mr F.S. Nariman, learned counsel appearing for BPL in the foremost argues by way of preliminary submissions that three questions will arise at the threshold.

(a) The scope and ambit of judicial review with regard to decisions bona fide arrived at in tender cases (pre- contract).

(b) The applicability of judicial review in these cases.

(c) The interference under Article 136 of the Constitution where the power of judicial review has been exercised by the High Court under Article 226.

47. It is submitted that the reasonableness in administrative law means to distinguish between proper use or improper use of power. The test is not the court's own standard of reasonableness. This Court has reiterated this proposition in G.B. Mahajan v. Jalgaon Municipal Council12. There is a possibility of fallibility inherent in all fact- findings. To insist upon a strict compliance with each and every tender document is not the law. This Court upheld the waiver of technical, literal compliance of the tender conditions in Poddar Steel Corn. v. Ganesh Engineering Works 1 3. In the present case, the short-listing at the first stage, the allotment of cities at the second stage and the selection of franchisees qua cities at the third stage were after evaluating the financial bid by a collectivity of persons at different level. Therefore, possibility of elimination of arbitrariness is conceived in the system itself. Further, the High Court has analysed properly and come to the proper conclusion. That being so, this Court will not interfere by exercising its powers under Article 136 of the Constitution of India. The argument about hidden criteria would not affect or benefit this respondent directly or indirectly. Even otherwise, the hidden criteria cannot be impugned. There is no mention of any particular criterion on the basis of which the selection was to be made. At the second stage what was required to be kept in mind were the parameters mentioned in paragraph 2.4. The criteria for selection to each of the four cities had to be provided inter alia because the tenderer did not tender for one city alone but for more than one. The allegation of bias on the 12 (1991) 3 SCC 91 (para 43-46) 13 (1991) 3 SCC 273 part of Mr Nair is without substance. It is submitted, whenever disqualification on the ground of personal involvement is alleged :

(i) the person involved (for example related) must be the decision-maker;

(ii) there must be sufficient nexus between the decision- maker and the party complaining in order to justify the real likelihood of bias.

48. After a decision is reached the standard of proof of bias is higher as laid down in Vassiliades v. Vassiliades14. This decision has been referred to by this Court in Ranjit Thakur v. Union of India 15. The learned counsel after referring to the relevant case law submits that cases of bias and ostensible bias had to be regarded in the light of their own circumstances. In this case Mr Subhash Nair is only one of the officers in BPL, which has over 5500 employees and 89 officers of his rank in 27 offices all over India. Mr Nair was not the decision-maker at all. He was one of the recommending authorities. His involvement in the approval and selection of the tender was indispensable. He was originally the Member (Services) on 29-5-1992. Thereafter he became Director General, Telecommunications by a notification issued by 28-7-1992 by the President of India. As such, he was to exercise all powers of Telegraph Authority under Section 3(6) of the Act. Therefore, the High Court was right in applying the doctrine of necessity. This doctrine has come up for discussion in Charan Lal Sahu v. Union of India 16.

49. Whatever it may be, Indian Telecom cannot take the point of bias. It took the chance and benefit of being short-listed despite the knowledge of Mr Nair's involvement. Equally, Tata Cellular did not raise the allegation of bias in the High Court. In fact, it opposed the plea of bias.

50. No doubt, this respondent dropped McCaw as a foreign collaborator. That does not amount to change where one out of two or three collaborators is dropped. This foreign collaborator was required as Condition No. 7 only in financial bid documents not in tender documents. This respondent submitted financial bid on 17-8-1992 showing only two of the collaborators. McCaw was not shown as that was already dropped out. Therefore, the High Court rightly held that McCaw was not taken into consideration in awarding marks for foreign partners' experience. The object of the first stage was not to allot the franchise but to short-list the parties.

51. The learned Solicitor General produced the copies of the relevant documents in the file and took us through the same. It is submitted, after outlining the process of evaluation in the second stage six parameters were adopted by the Committee consisting of Telecom experts who are none other than the senior officers of the Department of Telecommunications. The parameters are as follows :

1. Quoted rental ceiling 14 AIR 1945 PC 38: 221 IC 603: 1945 All LJ 34 15 (1987) 4 SCC 611: 1988 SCC (L&S) 1: (1987) 5 ATC 11 3: (1988) 1 SCR 512 16 (1990) 1 SCC 613

2. Project financing plan 3 . Foreign Exchange inflow and outflow

4. Project's plan for cellular equipment within the country including the tie-up with the proposed Indian manufacturers.

5 . Experience of foreign operating partner and

6. Financial strength of parameters/partner companies. These parameters were assigned marks. The evaluation report including the ranking arrived at by the tender evaluation committee was then put up to the Telecom Commission for further consideration and selection. Due to technical considerations not more than two bidders per city could be accommodated. Paragraph 14 of the bid conditions provided that each bidder must furnish a declaration in a specified form to the bid documents. The declaration given by Hutchison Max was complete. However, its bid had to be rejected on merits in spite of securing high marks.

52. M/s India Telecomp secured the second place for Calcutta. Inasmuch as they had the same foreign partner as Usha Martin which secured a higher place than India Telecomp, it was rejected and the choice went to the next bidder in the marking list. After the above considerations were taken into account, the remaining companies were selected which led to the writ petition. Pursuant to the High Court directions the matter was reconsidered and selections have been made as was done earlier.

53. The principal objection of the Union of India is that the High Court was not justified in scrutinising the tendering process in such detail. The minute examination is unwarranted because the High Court cannot constitute itself the selecting authority. However, no appeal is preferred, as otherwise, it would have further delayed the introduction of very valuable communication facility in this country. Beyond that, it has no particular interest as to who is selected. However, it becomes necessary to answer the allegations made about the actual selection and whether there was any bias on the part of the selection committee. The selection process was dictated by the, exigencies of the situation. It is a question, as to what one could settle for, in the given circumstances. The Government was embarking upon a totally new technology project, for the first time. At that stage, it was impossible to predict what kind of response will there be. Therefore, it is impossible to predicate the cut-off limits which could be set or which conditions have to be relaxed or softened. The allegation of bias, it is held, must be a case of reasonable possibility or likelihood of bias. In this case, there is no such reasonable likelihood. Mr B.R. Nair was not influenced directly, or, in any other manner, subtle or otherwise. He did not, in fact, participate in any of the significant or crucial stages in the selection process. Even otherwise, the relationship is not such as to give reasonable apprehension of bias. In support of this argument reliance is placed on Manak Lal and Ashok Kumar Yadav v. State of Haryana3 (SCC p. 441, para 16). As regards the parameter in relation to project financing it was kept in view by taking into account the estimated number of subscribers, installation charges, monthly rental, any other charges etc. They were included in the competition. The other parameters of the bidders were treated on the same footing as regards this parameter is concerned. Concerning rental, it was specifically averred in the counter before the High Court that the other charges had also been included while calculating quoted rental.

54. It is not correct to contend that Talkland's experience is not relevant. In the United Kingdom the operation of Mobile Cellular System is handled by the network cooperator and a proper service provider, acting together. The licensee is required to perform the combined functions of a network operator as well as service provider. The duties and functions of a licensee are not limited to making available the services as defined. In fact, the principal obligation of the licensee is expressed generally in paragraph 2. 1. 1. A reading of the other clauses makes it clear that it is incumbent upon the licensee to provide services. Therefore, the experiences of a network operator and the service provider are both important and relevant.

55. In the case of Bharati Cellular the attack is that the cut-off came to be reduced to 80,000 subscribers to accommodate it. Bharati Cellular mentioned in its tender, as on 31-12-1991, the name of SFR France which had 80,000 subscribers. By 31-12-1991, it would have got increased to more than one lakh. In August 1992 when the bids were submitted SFR's line of experience could reasonably be expected to be more than one lakh. SFR France had a GSM licence. Having regard to these facts, it would not be an unreasonable estimate, for the experts, to conclude that Bharati Cellular was having experience of over one lakh lines.

56. It is alleged that the debt/equity ratio of Skycell has not been properly taken. Skycell ratio was 1.5 and was correctly assigned 3 marks.

57. Tata Cellular alleges that Bharati Cellular, Mobile Telecom, Sterling and Skycell have breached note (ii) under para 2.4 which provides that minimum reliance on Indian Public Financial Institutions will be preferred. The bid profess made distinction between loans from Public Financial Institutions and Banks. The criticism of Tata confuses this requirement with loan from Banks. The criterion, it is submitted, was correctly applied.

58. In the evaluation of process open market purchase was left out of consideration.

59. Since Skycell bid for Madras showed that they had projected their operations in Madras for initial years, would be below profitable levels. In such a case, no dividend would have to be paid to the foreign collaborators. Accordingly, it was concluded that the foreign exchange inflow position was better.

60. International roaming is a relevant consideration. From the tender document it will be clear that it provides for facility of roaming to visitors. Roaming facility for a tourist is available in the GSM system. Even if this condition has been relaxed in favour of certain bidders, there is nothing wrong. Reliance is placed on G.J. Fernandez v. State of Kamatakal7.

61. With regard to the foreign collaborator of BPL there was no change. French Telecom is one of the foremost in the world in this technology. It remained as foreign collaborator of BPL. Dropping out of McCaw did not violate the bid conditions which were really aimed at preventing a new and, therefore, unknown collaborator being introduced at the financial bid stage. The second Technical Evaluation Committee did not see this as a violation. In any event, where the judgment of the High Court had been given effect to and a proper evaluation has been done, no interference is warranted.

62. Mr Soli J. Sorabjee, learned counsel, in his reply, would submit that as regards the scope of judicial review the American cases cited by Mr K.K. Venugopal would not apply. As laid down in State of U.P v. Maharaja Dharmander Prasad Singh18 judicial review is confined to decision- making process. This being an administrative action the scope of judicial review could be gathered from Council of Civil Service Unions v. Minister for Civil Service19. In Secy. of State for Education and Science v. Tameside Metropolitan Borough Council2O the law has been stated as to when subjective satisfaction could be interfered with under judicial review. This Court also had occasion to deal with similar contracts and stated the law relating to judicial review in Sterling Computers Ltd. v. M&N Publications Ltd.5 (SCC pp. 455 and 458, para 19) and then again, in Union of India v. Hindustan Development Corpn.6

63. The point against Hutchison Max is, the defect in its tender, came to be pointed out, requiring it to comply with the same. In view of the defect Hutchison Max came to be excluded.

64. Mr Nair's participation from the beginning would constitute bias in law.

65. Mr Ashoke Sen, in his reply, would state that in the case of Hutchison Max the mistake was committed in the offer with regard to compliance statement. The principle of bias as laid down in R. v. Essex Justices (Sizer), ex p Perkins21 would apply. Similar passage occurs in de Smith's Constitutional and Administrative Law (4th Edn.) p. 268.

66. Mr Harish Salve, in reply, would urge that the hidden criteria were evolved in relation to common foreign collaborator. This shows that there was lack of candour on the part of the Union. It is mentioned that Talkland was taken into consideration. It is not so, as seen from the file. The conditions were tailor-made to suit Bharati Cellular and BPL.

17 (1990) 2 SCC 488 (para 18) 18 (1989) 2 SCC 505, 524: (1989) 1 SCR 176, 202 19 (1985) 1 AC 374: (1984) 3 All ER 935: (1984) 3 WLR 1174 20 1977 AC 1014: (1976) 3 All ER 665: (1976) 3 WLR 641 21 (1927) 2 KB 475: 1927 All ER Rep 393: 96 UKB 530

67. Mr K.K. Venugopal would urge that the rule relating to judicial review should not be applied here because it is one of selection by an a administrative process.

68. Having regard to the above arguments we propose to deal with the matter from the following five aspects :

1. The scope of judicial review in matters of this kind.

2. Whether the selection is vitiated by arbitrariness?

(a) regarding financial projection and (b) regarding rental.

3. Bias of Mr Nair whether affected the selection ?

4. Whether the Apex Committee has been bypassed?

5. Evolving of hidden criteria whether valid?

1. Scope of Judicial Review

69. A tender is an offer. It is something which invites and is communicated to notify acceptance. Broadly stated, the following are the requisites of a valid tender :

1. It must be unconditional.

2. Must be made at the proper place.

3. Must conform to the terms of obligation.

4. Must be made at the proper time.

5. Must be made in the proper form.

6. The person by whom the tender is made must be able and willing to perform his obligations.

7. There must be reasonable opportunity for inspection.

8. Tender must be made to the proper person.

9. It must be of full amount.

70. It cannot be denied that the principles of judicial review would apply to the exercise of contractual powers by Government bodies in order to prevent arbitrariness or favoritism. However, it must be clearly stated that there are inherent limitations in exercise of that power of judicial review. Government is the guardian of the finances of the State. It is expected to protect the financial interest of the State. The right to refuse the lowest or any other tender is always available to the Government. But, the principles laid down in Article 14 of the Constitution have to be kept in view while accepting or refusing a tender. There can be no question of infringement of Article 14 if the Government tries to get the best person or the best quotation. The right to choose cannot be considered to be an arbitrary power. Of course, if the said power is exercised for any collateral purpose the exercise of that power will be struck down.

71. Judicial quest in administrative matters has been to find the right balance between the administrative discretion to decide matters whether contractual or political in nature or issues of social policy; thus they are not essentially justifiable and the need to remedy any unfairness. Such an unfairness is set right by judicial review.

72. Lord Scarman in Nottinghamshire County Council v. Secretary of State for the Environment22 proclaimed :

" 'Judicial review' is a great weapon in the hands of the judges; but the judges must observe the constitutional limits set by our parliamentary system upon the exercise of this beneficial power."

Commenting upon this Michael Supperstone and James Goudie in their work Judicial Review (1992 Edn.) at p. 16 say :

"If anyone were prompted to dismiss this sage warning as a mere obiter dictum from the most radical member of the higher judiciary of recent times, and therefore to be treated as an idiosyncratic aberration, it has received the endorsement of the Law Lords generally. The words of Lord Scarman were echoed by Lord Bridge of Harwich, speaking on behalf of the Board when reversing an interventionist decision of the New Zealand Court of Appeal in Butcher v. Petrocorp Exploration Ltd. 18-3- 1991."

73. Observance of judicial restraint is currently the mood in England. The judicial power of review is exercised to rein in any unbridled executive functioning. The restraint has two contemporary manifestations. One is the ambit of judicial intervention; the other covers the scope of the court's ability to quash an administrative decision on its merits. These restraints bear the hallmarks of judicial control over administrative action.

74. Judicial review is concerned with reviewing not the merits of the decision in support of which the application for judicial review is made, but the decision-making process itself.

75. In Chief Constable of the North Wales Police v. Evans23 Lord Brightman said :

"Judicial review, as the words imply, is not an appeal from a decision, but a review of the manner in which the decision was made. Judicial review is concerned, not with the decision, but with the decision-making process. Unless that restriction on the power of the court is observed, the court will in my view, under the guise of preventing the abuse of power, be itself guilty of usurping power."

In the same case Lord Hailsham commented on the purpose of the remedy by way of judicial review under RSC, Ord. 53 in the following terms :

"This remedy, vastly increased in extent, and rendered, over a long period in recent years, of infinitely more convenient access than that provided by the old prerogative writs and actions for a declaration, is intended to protect the individual against the abuse of power by a wide range of authorities, judicial, quasi-judicial, and, as would originally have been thought when I first practiced at the Bar, administrative. It is not intended to take away from those authorities the powers and 22 1986 AC 240, 251: (1986) 1 All ER 199 23 (1982) 3 All ER 141, 154 discretions properly vested in them by law and to substitute the courts as the bodies making the decisions. It is intended to see that the relevant authorities use their powers in a proper manner (p. 1160)."

In R. v. Panel on Takeovers and Mergers, ex p Datafin plc24, Sir John Donaldson, M.R. commented:

"An application for judicial review is not an appeal." In Lonrho plc v. Secretary of State for Trade and Industry25, Lord Keith said: "Judicial review is a protection and not a weapon."

It is thus different from an appeal. When hearing an appeal the Court is concerned with the merits of the decision under appeal. In Amin, Re26, Lord Fraser observed that :

"Judicial review is concerned not with the merits of a decision but with the manner in which the decision was made.... Judicial review is entirely different from an ordinary appeal. It is made effective by the court quashing the administrative decision without substituting its own decision, and is to be contrasted with an appeal where the appellate tribunal substitutes its own decision on the merits for that of the administrative officer."

76. In R. v. Panel on Take-overs and Mergers, ex p in Guinness plc27, Lord Donaldson, M.R. referred to the judicial review jurisdiction as being supervisory or 'longstop' jurisdiction. Unless that restriction on the power of the court is observed, the court will, under the guise of preventing the abuse of power, be itself guilty of usurping power.

77. The duty of the court is to confine itself to the question of legality. Its concern should be :

1. Whether a decision-making authority exceeded its powers?

2. Committed an error of law,

3. committed a breach of the rules of natural justice,

4. reached a decision which no reasonable tribunal would have reached or,

5. abused its powers.

Therefore, it is not for the court to determine whether a particular policy or particular decision taken in the fulfillment of that policy is fair. It is only concerned with the manner in which those decisions have been taken. The extent of the duty to act fairly will vary from case to case. Shortly put, the grounds upon which an administrative action is subject to control by judicial review can be classified as under:

24 (1987) 1 All ER 564 25 (1989) 2 All ER 609 26 Amin v. Entry Clearance Officer, (1983) 2 All ER 864 27 (1990) 1 QB 146: (1989) 1 All ER 509

(i) Illegality : This means the decision- maker must understand correctly the law that regulates his decision-making power and must give effect to it.

(ii) Irrationality, namely, Wednesday unreasonableness.

(iii) Procedural impropriety.

The above are only the broad grounds but it does not rule out addition of further grounds in course of time. As a matter of fact, in R. v. Secretary of State for the Home Department, ex Brind28, Lord Diplock refers specifically to one development, namely, the possible recognition of the principle of proportionality. In all these cases the test to be adopted is that the court should, "consider whether something has gone wrong of a nature and degree which requires its intervention".

78. What is this charming principle of Wednesday unreasonableness? Is it a magical formula? In R. v. Askew29, Lord Mansfield considered the question whether mandamus should be granted against the College of Physicians. He expressed the relevant principles in two eloquent sentences. They gained greater value two centuries later :

"It is true, that the judgment and discretion of determining upon this skill, ability, learning and sufficiency to exercise and practise this profession is trusted to the College of Physicians and this Court will not take it from them, nor interrupt them in the due and proper exercise of it. But their conduct in the exercise of this trust thus committed to them ought to be fair, candid and unprejudiced; not arbitrary, capricious, or biased; much less, warped by resentment, or personal dislike."

79. To quote again, Michael Supperstone and James Goudie; in their work Judicial Review (1992 Edn.) it is observed at pp. 119 to 121 as under :

"The assertion of a claim to examine the reasonableness been done by a public authority inevitably led to differences of judicial opinion as to the circumstances in which the court should intervene. These differences of opinion were resolved in two landmark cases which confined the circumstances for intervention to narrow limits. In Kruse v. Johnson3O a specially constituted divisional court had to consider the validity of a bye- law made by a local authority. In the leading judgment of Lord Russell of Killowen, C.J., the approach to be adopted by the court was set out. Such bye-laws ought to be 'benevolently' interpreted, and credit ought to be given to those who have to administer them that they would be reasonably administered. They could be held invalid if unreasonable : Where for instance bye-laws were found to be partial and unequal in their operation as between different classes, if they were manifestly unjust, if they disclosed bad faith, or if they involved such oppressive or gratuitous interference with the rights of citizens as could find no justification in the minds of reasonable men. Lord Russell 28 (1991) 1 AC 696 29 (1768) 4 Burr 2186 : 98 ER 139 30 (1898) 2 QB 91: (1895-9) All ER Rep 105 emphasised that a bye-law is not unreasonable just because particular judges might think it went further than was prudent or necessary or convenient.

In 1947 the Court of Appeal confirmed a similar approach for the review of executive discretion generally in Associated Provincial Picture Houses Ltd. v. Wednesbury Corpn31. This case was concerned with a complaint by the owners of a cinema in Wednesbury that it was unreasonable of the local authority to licence performances on Sunday only subject to a condition that 'no children under the age of 15 years shall be admitted to any entertainment whether accompanied by an adult or not'. In an extempore judgment, Lord Greene, M.R. drew attention to the fact that the word 'unreasonable' had often been used in a sense which comprehended different grounds of review. (At p. 229, where it was said that the dismissal of a teacher for having red hair (cited by Warrington, L.J. in Short v. Poole Corpn.32, as an example of a 'frivolous and foolish reason') was, in another sense, taking into consideration extraneous matters, and might be so unreasonable that it could almost be described as being done in bad faith; see also R. v. Tower Hamlets London Borough Council, ex p Chetnik Developments Ltd.33 (Chapter 4, p. 73, supra). He summarised the principles as follows:

"The Court is entitled to investigate the action of the local authority with a view to seeing whether or not they have taken into account matters which they ought not to have taken into account, or, conversely, have refused to take into account or neglected to take into account matter which they ought to take into account. Once that question is answered in favour of the local authority, it may still be possible to say that, although the local authority had kept within the four comers of the matters which they ought to consider, they have nevertheless come to a conclusion so unreasonable that no reasonable authority could ever have come to it. In such a case, again, I think the court can interfere. The power of the court to interfere in each case is not as an appellate authority to override a decision of the local authority, but as a judicial authority which is concerned, and concerned only, to see whether the local authority has contravened the law by acting in excess of the power which Parliament has confided in them.' This summary by Lord Greene has been applied in countless subsequent cases.

"The modem statement of the principle is found in a passage in the speech of Lord Diplock in Council of Civil Service Unions v. Minister for Civil Service19:

31 (1948) 1 KB 223: (1947) 2 All ER 680 32 (1926) 1 Ch 66, 91: 1925 All ER Rep 74 33 1988 AC 858, 873: (1988) 2 WLR 654: (1988) 1 All ER 961 'By "irrationality" I mean what can now be succinctly referred to as "Wednesbury unreasonableness". (Associated Provincial Picture Houses Ltd. v. Wednesbury Corpn.31) It applies to a decision which is so outrageous in its defiance of logic or of accepted moral standards that no sensible person who had applied his mind to the question to be decided could have arrived at.' "

80. At this stage, The Supreme Court Practice, 1993, Vol.

1, pp. 849850, may be quoted :

"4. Wednesbury principle.- A decision of a public authority will be liable to be quashed or otherwise dealt with by an appropriate order in judicial review proceedings where the court concludes that the decision is such that no authority properly directing itself on the relevant law and acting reasonably could have reached it. (Associated Provincial Picture Houses Ltd. v. Wednesbury Corpn. 3 1, per Lord Greene, M.R.)"

81. Two other facets of irrationality may be mentioned. (1) It is open to the court to review the decision-maker's evaluation of the facts. The court will intervene where the facts taken as a whole could not logically warrant the conclusion of the decision-maker. If the weight of facts pointing to one course of action is overwhelming, then a decision the other way, cannot be upheld. Thus, in Emma Hotels Ltd. v. Secretary of State for Environment34, the Secretary of State referred to a number of factors which led him to the conclusion that a non-resident's bar in a hotel was operated in such a way that the bar was not an incident of the hotel use for planning purposes, but constituted a separate use. The Divisional Court analysed the factors which led the Secretary of State to that conclusion and, having done so, set it aside. Donaldson, L.J. said that he could not see on what basis the Secretary of State had reached his conclusion.

(2) A decision would be regarded as unreasonable if it is impartial and unequal in its operation as between different classes. On this basis in R. v. Bernet London Borough Council, ex p Johnson35 the condition imposed by a local authority prohibiting participation by those affiliated with political parties at events to be held in the authority's parks was struck down.

82. Bernard Schwartz in Administrative Law, 2nd Edn., p. 584 has this to say :

" If the scope of review is too broad, agencies are turned into little more than media for the transmission of cases to the courts. That would destroy the values of agencies created to secure the benefit of special knowledge acquired through continuous administration in complicated fields. At the same time, the scope of judicial inquiry must not be so restricted that it prevents full inquiry into the question of legality. If that question cannot be properly explored by the judge, the right to review becomes meaningless. 'It makes judicial review of administrative orders 34 (1980) 41 P & CR 255 35 (1989) 88 LGR 73 a hopeless formality for the litigant.... It reduces the judicial process in such cases to a mere feint.' Two overriding considerations have combined to narrow the scope of review. The first is that of deference to the administrative expert. In Chief Justice Neely's words :

'I have very few illusions about my own limitations as a judge and from those limitations I generalize to the inherent limitations of all appellate courts reviewing rate cases. It must be remembered that this Court sees approximately 1262 cases a year with five judges. I am not an accountant, electrical engineer, financier, banker, stock broker, or systems management analyst. It is the height of folly to expect judges intelligently to review a 5000 page record addressing the intricacies of public utility operation.' It is not the function of a judge to act as a superboard, or with the zeal of a pedantic schoolmaster substituting its judgment for that of the administrator. The result is a theory of review that limits the extent to which the discretion of the expert may be scrutinised by the non-expert judge. The alternative is for the court to overrule the agency on technical matters where all the advantages of expertise lie with the agencies, If a court were to review fully the decision of a body such as state board of medical examiners 'it would find itself wandering amid the maze of therapeutics or boggling at the mysteries of the Pharmacopoeia'. Such a situation as a state court expressed it many years ago 'is not a case of the blind leading the blind but of one who has always been deaf and blind insisting that he can see and hear better than one who has always had his eyesight and hearing and has always used them to the utmost advantage in ascertaining the truth in regard to the matter in question'.

The second consideration leading to narrow review is that of calendar pressure. In practical terms it may be the more important consideration. More than any theory of limited review it is the pressure of the judicial calendar combined with the elephantine bulk of the record in so many review proceedings which leads to perfunctory affirmably of the vast majority of agency decisions."

83. A modem comprehensive statement about judicial review by Lord Denning is very apposite; it is perhaps worthwhile noting that he stresses the supervisory nature of the jurisdiction :

"Parliament often entrusts the decision of a matter to a specified person or body, without providing for any appeal. It may be a judicial decision, or a quasi-judicial decision, or an administrative decision. Sometimes Parliament says its decision is to be final. At other times it says nothing about it. In all these cases the courts will not themselves take the place of the body to whom Parliament has entrusted the decision. The courts will not themselves embark on a rehearing of the matter. See Healey v. Minister of Health36. But nevertheless, the courts will, if called upon, act in a supervisory capacity. They will see that the decision-making body acts fairly. See H.K. (an infant), Re37, and R. V. Gaming Board for Great Britain, ex p Benaim and Khaida38. The courts will ensure that the body acts in accordance with the law. If a question arises on the interpretation of words, the courts will decide it by declaring what is the correct interpretation. See Punton v. Ministry of Pensions and National Insurance39. And if the decision-making body has gone wrong in its interpretation they can set its order aside. See Ashbridge Investments Ltd. v. Minister of Housing and Local Government40. I know of some expressions to the contrary but they are not correct). If the decision-making body is influenced by considerations which ought not to influence it; or fails to take into account matters which it ought to take into account, the court will interfere. See Padfield v. Minister of Agriculture, Fisheries and Food41. If the decision-making body comes to its decision on no evidence or comes to an unreasonable finding so unreasonable that a reasonable person would not have come to it then again the courts will interfere. See Associated Provincial Picture Houses Ltd. v. Wednesbury Corpn.31 If the decision making body goes outside its powers or misconstrues the extent of its powers, then, too the courts can interfere. See Anisminic Ltd. v. Foreign Compensation Commission42. And, of course, if the body acts in bad faith or for an ulterior object, which is not authofised by law, its decision will be set aside. See Sydney Municipal Council v. Campbell43. In exercising these powers, the courts will take into account any reasons which the body may give for its decisions. If it gives no reasons in a case when it may reasonably be expected to do so, the courts may infer that it has no good reason for reaching its conclusion, and act accordingly. See Padfield case (as AC pp. 1007, 1061)41."

84. We may usefully refer to Administrative Law Rethinking Judicial Control of Bureaucracy by Christopher F. Edley, JR (1990 Edn.). At p. 96 it is stated thus :

"A great deal of administrative law boils down to the scope of review problem; defining what degree of deference a court will accord to an agency's findings, conclusions, and choices, including choice of procedures. It is misleading to speak of a 'doctrine', or 'the law', of scope of review. It is instead just a big problem, that is addressed 36 (1955) 1 QB 221: (1954) 3 All ER 449: (1954) 3 WLR 815 37 (1967) 2 QB 617,630: (1967) 1 All ER 226: (1967) 2 WLR 38 (1970) 2 QB 417: (1970) 2 All ER 528: (1970) 2 WLR 1009 39 (1963) 1 WLR 186: (1963) 1 All ER 275 40 (1965) 1 WLR 1320: (1965) 3 All ER 371 41 1968 AC 997: (1968) 1 All ER 694 42 (1969) 2 AC 147: (1969) 1 All ER 208: (1969) 2 WLR 163 43 1925 AC 338: 1924 All ER Rep 930 piecemeal by a large collection of doctrines. Kenneth Culp Davis has offered a condensed summary of the subject:

'Courts usually substitute (their own) judgment on the kind of questions of law that are within their special competence, but on other question they limit themselves to deciding reasonableness; they do not clarify the meaning of reasonableness but retain full discretion in each case to stretch it in either direction.' "

85. In Universal Camera Corpn. v. National Labor Relations Board44 Justice Frankfurter stated :

"A formula for judicial review of administrative action may afford grounds for certitude but cannot assure certainty of application. Some scope for judicial discretion in applying the formula can be avoided only by falsifying the actual process of judging or by using the formula as an instrument of futile casuistry. It cannot be too often repeated that judges are not automata. The ultimate reliance for the fair operation of any standard is a judiciary of high competence and character and the constant play of an informed professional critique upon its work. Since the precise way in which courts interfere with agency findings cannot be imprisoned within any form of words, new formulas attempting to rephrase the old are not likely to be more helpful than the old. There are no talismanic words that can avoid the process of judgment. The difficulty is that we cannot escape, in relation to this problem, the use of undefined defining terms."

86. An innovative approach is made by Clive Lewis as to why the courts should be slow in quashing administrative decisions (in his Judicial Remedies in Public Law 1992 Edn. at pp. 294-95). The illuminating passage reads as under :

"The courts now recognise that the impact on the administration is relevant in the exercise of their remedial jurisdiction.

Quashing decisions may impose heavy administrative burdens on the administration, divert resources towards reopening decisions, and lead to increased and unbudgeted expenditure. Earlier cases took the robust line that the law had to be observed, and the decision invalidated whatever the administrative inconvenience caused. The courts nowadays recognise that such an approach is not always appropriate and may not be in the wider public interest. The effect on the administrative, process is relevant to the courts' remedial discretion and may prove decisive. This is particularly the case when the challenge is procedural rather than substantive, or if the courts can be certain that the administrator would not reach a different decision even if the original decisions were quash ed.

Judges may differ in the importance they attach to the disruption that quashing a decision will cause. They may also be influenced by the extent to which the illegality arises from the conduct of the administrative body itself, and their view of that conduct. 44 340 US 474, 488-89: 95 L Ed 456 (1950) The current approach is best exemplified by R. v. Monopolies and Mergers Commission, ex p Argyll Group plc45. "

87. Sir John Donaldson, M.R. in R. v. Monopolies and Mergers Commission, ex p Argyll Group plc45 observed thus :

"We are sitting as a public law court concerned to review an administrative decision, albeit one which has to be reached by the application of judicial or quasi- judicial principles. We have to approach our duties with a proper awareness of the needs of public administration. I cannot catalogue them all but, in the present context, would draw attention to a few which are relevant. Good public administration is concerned with substance rather than form.

of decision, particularly in the financial field.

consideration of the public interest. In this context, the Secretary of State is the guardian of the public interest. consideration of the legitimate interests of individual citizens, however rich and powerful they may be and whether they are natural or juridical persons. But in judging the relevance of an interest, however legitimate, regard has to be had to the purpose of the administrative process concerned. and finality, unless there are compelling reasons to the contrary."

88. We may now look at some of the pronouncements of this Court including the authorities cited by Mr Ashoke Sen. Fasih Chaudhary v. Director General, Doordarshan46 was a case in which the Court was concerned with the award of a contract for show of sponsored TV serial. At p. 92 in paragraphs 5 and 6 it was held thus :

"It is well settled that there should be fair play in action in a situation like the present one, as was observed by this Court in Ram & Shyam Co. v. State of Haryana47. It is also well settled that the authorities like Doordarshan should act fairly and their action should be legitimate and fair and transaction should be without any aversion, malice or affection. Nothing should be done which gives the impression of favoritism or nepotism. See the observations of this Court in Haji TM. Hassan Rawther v. Kerala Financial Corpn.48 While, as mentioned herein before, fair play in action in matters like the present one is an essential requirement, similarly, however, 'free play in the joints' is also a necessary concomitant for an administrative body 45 (1986) 1 WLR 736, 774: (1986) 2 All ER 257, CA 46 (1989) 1 SCC 89 47 (1985) 3 SCC 267, 268-69 48 (1988) 1 SCC 166, 173 (para 14) functioning in an administrative sphere or quasi-administrative sphere as the present one. Judged from that standpoint of view, though all the proposals might not have been considered strictly in accordance with order of precedence, it appears that these were considered fairly, reasonably, objectively and without any malice or ill-will."

89. In G.B. Mahajan v. Jalgaon Municipal Council12 the concept of reasonableness in administrative law came to be dealt with elaborately by one of us, Venkatachaliah, J. (as he then was). In paragraphs 37 to 41 the Court observed thus :

"It was urged that the basic concept of the manner of the development of the real estate and disposal of occupancy rights were vitiated by unreasonableness. It is a truism, doctrinally, that powers must be exercised reasonably. But as Prof. Wade points out :

'The doctrine that powers must be exercised reasonably has to be reconciled with the no less important doctrine that the court must not usurp the discretion of the public authority which Parliament appointed to take the decision. Within the bounds of legal reasonableness is the area in which the deciding authority has genuinely free discretion. If it passes those bounds, it acts ultra vires. The court must therefore resist the temptation to draw the bounds too tightly, merely according to its own opinion. It must strive to apply an objective standard which leaves to the deciding authority the full range of choices which the legislature is presumed to have intended. Decisions which are extravagant or capricious cannot be legitimate, But if the decision is within the confines of reasonableness, it is no part of the court's function to look further into its merits. "With the question whether a particular policy is wise or foolish the court is not concerned; it can only interfere if to pursue it is beyond the powers of the authority"...

In the arguments there is some general misapprehension of the scope of the 'reasonableness' test in administrative law. By whose standards of reasonableness that a matter is to be decided? Some phrases which pass from one branch of law to another as did the expressions 'void' and ,voidable' from private law areas to public law situations carry over with them meanings that may be inapposite in the changed context. Some such thing has happened to the words "reasonable', ,reasonableness' etc. In Tiller v. Atlantic Coast Line Rail Road Co.49, Justice Frankfurter said :

'A phrase begins life as a literary expression; its felicity leads to its lazy repetition; and repetition soon establishes it as a legal formula, undiscriminatingly used to express different and sometimes contradictory ideas.' Different contexts in which the operation of 'reasonableness' as test of validity operates must be kept distinguished. For instance as the 49 318 US 54: 87 L Ed 610 (1942) arguments in the present case invoke, the administrative law test of ,reasonableness' as the touchstone of validity of the impugned resolutions is different from the test of the 'reasonable man' familiar to the law of torts, whom English law figuratively identifies as the 'man on the Clapham omnibus'. In the latter case the standards of the 'reasonable man', to the extent such a 'reasonable man' is court's creation, is in a manner of saying, a mere transferred epithet. Lord Radcliffe observed (All ER p.

160) .lm15 'By this time, it might seem that the parties themselves have become so far disembodied spirits that their actual persons should be allowed to rest in peace. In their place there rises the figure of the fair and reasonable man. And the spokesman of the fair and reasonable man, who represents after all no more than the anthropomorphic conception of justice, is, and must be, the court itself....' (emphasis supplied) See Davis Contractors Ltd. v. Fareham U.D. C.50 Yet another area of reasonableness which must be distinguished is the constitutional standards of 'reasonableness' of the restrictions on the fundamental rights of which the court of judicial review is the arbiter. The administrative law test of reasonableness is not by the standards of the 'reasonable man' of the torts law. Prof. Wade says :

'This is not therefore the standard of "the man on the Clapham omnibus". It is the standard indicated by a true construction of the Act which distinguishes between what the statutory authority may or may not be authorised to do. It distinguishes between proper use and improper abuse of power. It is often expressed by saying that the decision is unlawful if it is one to which no reasonable authority could have come. This is the essence of what is now commonly called "Wednesbury unreasonableness", after the now famous case in which Lord Greene, MR. expounded it."' (emphasis supplied)

90. Referring to the doctrine of unreasonableness, Prof. Wade says in Administrative Law (supra) : "The point to note is that a thing is not unreasonable in the legal sense merely because the court thinks it is unwise."

91. In Food Corpn. of India v. Kamdhenu Cattle Feed Industries51 it was observed thus : (SCC p. 76, para 7) "In contractual sphere as in all other State actions, the State and all its instrumentalities have to conform to Article 14 of the Constitution of which non-

arbitrariness is a significant facet. There is no unfettered discretion in public law : A public authority possesses powers only to use them for public good. This imposes the duty to act fairly and to adopt a procedure which is 'fairplay in action'."

50 (1956) 2 All ER 145, 160: 1956 AC 696: (1956) 3 WLR 37 51 (1993) 1 SCC 71

92. In Sterling Computers Limited v. M&N Publications Ltd.5 this Court observed thus : (SCC p. 455, para 12) "In contracts having commercial element, some more discretion has to be conceded to the authorities so that they may enter into contracts with persons, keeping an eye on the augmentation of the revenue. But even in such matters they have to follow the norms recognised by courts while dealing with public property. It is not possible for courts to question and adjudicate every decision taken by an authority, because many of the Government Undertakings which in due course have acquired the monopolist position in matters of sale and purchase of products and with so many ventures in hand, they can come out with a plea that it is not always possible to act like a quasi-judicial authority while awarding contracts. Under some special circumstances a discretion has to be conceded to the authorities who have to enter into contract giving them liberty to assess the overall situation for purpose of taking a decision as to whom the contract be awarded and at what terms. If the decisions have been taken in bona fide manner although not strictly following the norms laid down by the courts, such decisions are upheld on the principle laid down by Justice Holmes, that courts while judging the constitutional validity of executive decisions must grant certain measure of freedom of 'play in the joints' to the executive."

93. In Union of India v. Hindustan Development Corpn.6 this Court held thus : (SCC p. 515, para 9) "... the Government had the right to either accept or reject the lowest offer but that of course, if done on a policy, should be on some rational and reasonable grounds. In Erusian Equipment & Chemicals Ltd. v. State of W.B.9 this Court observed as under: (SCC p. 75, para

17) 'When the Government is trading with the public, "the democratic form of Government demands equality and absence of arbitrariness and discrimination in such transactions". The activities of the Government have a public element and, therefore, there should be fairness and equality. The State need not enter into any contract with anyone, but if it does so, it must do so fairly without discrimination and without unfair procedure.'

94. The principles deducible from the above are : (1) The modem trend points to judicial restraint in administrative action.

(2) The court does not sit as a court of appeal but merely reviews the manner in which the decision was made. (3) The court does not have the expertise to correct the administrative decision. If a review of the administrative decision is permitted it will be substituting its own decision, without the necessary expertise which itself may be fallible.

(4) The terms of the invitation to tender cannot be open to judicial scrutiny because the invitation to tender is in the realm of contract.

Normally speaking, the decision to accept the tender or award the contract is reached by process of negotiations through several tiers. More often than not, such decisions are made qualitatively by experts.

(5) The Government must have freedom of contract. In other words, a fair play in the joints is a necessary concomitant for an administrative body functioning in an administrative sphere or quasi-administrative sphere. However, the decision must not only be tested by the application of Wednesbury principle of reasonableness (including its other facts pointed out above) but must be free from arbitrariness not affected by bias or actuated by mala fides.

(6) Quashing decisions may impose heavy administrative burden on the administration and lead to increased and unbudgeted expenditure.

Based on these principles we will examine the facts of this case since they commend to us as the correct principles.

2. Whether the selection is vitiated by arbitrariness?

95. Mr Soli J. Sorabjee, learned counsel appearing for Tata Cellular argued that there are clear instances of arbitrariness. Criterion No. 2.4.7 has been totally ignored and excluded. This has been so admitted. No marks have been awarded on this score under this criterion. Note II of the same General Conditions 2.4.7 says minimum reliance on Indian Public Financial Institutions will be preferred. This requirement has been breached by Bharati Cellular, Mobile Telecom, Sterling Cellular and Skycell Communication. They have borrowed from commercial banks 4.87 per cent, 4.87 per cent, 43.48 per cent and 34.41 per cent respectively. This criterion carries 8 marks. In spite of the borrowings they have been awarded 6, 8 (full marks), 5 and 7 respectively. The company, Tata Cellular, which had not borrowed at all from the commercial banks, has been awarded only 4 marks. It requires to be noted that borrowing from commercial banks was prohibited by Reserve Bank of India.

96. Then again, one of the prescribed criterion is 2.4.6 which carries 12 marks, namely, the financial strength of the partner company. The annual turnover from Tata Cellular, from Indian parameters was 12,000 crores and annual turnover of their foreign parameters was 5 1,000 crores yet what has been awarded is only 9 marks. As against this Hutchison Max has only an annual turnover of 75 crores and Rupees 6600 crores of foreign parameters yet it has been awarded 12 marks. Equally, Sterling Cellular whose turnover according to its bid document was 77 crores; the foreign parameter is unknown, it has also been awarded 9 marks.

97. The cut-off date for financial bid document was fixed as 17-8-1992. To examine and evaluate the same a committee was set up. The committee adopted some parameters and devised a marking system. It is as under :

Purchase plan for Cellular equipment within the country including tie-ups with the proposed Indian manufacturers 5 Experience 15 Financial strength 12 Note : No marks were allotted for the seventh criterion of financial projections of Cellular Mobile Service. The report of the Tender Evaluation Committee on this aspect states as under :

"One of the parameters is about the financial projection. The Committee discussed about the reliability of financial projections made by the bidders and came to the conclusion that it is not possible for them to verify the reliability of the projections which are based on individual postulations about the number of subscribers, traffic, tariff, financial structure etc. For this purpose we have to go by the data furnished by the bidders at its face value. In any case the financial data, having relevance to evaluation of the tender have well been covered under various parameters."

Annexure 1 to the Report of the said Committee shows the manner in which parameters and their weighers were given to each criterion. The debt/equity ratio is 1.5 for city of Bombay. It has been rightly assigned 3 marks.

98.The bid pro forma of Bharati Cellular, Mobile Telecom, Sterling Cellularand Skycell indicates minimum reliance on financial institutions. It has alsomade distinction between loans from public financial institutions and banks. Therefore, there is a confusion on the part of Tata Cellular about this requirement with loans from the banks.

99.Records reveal that in the case of India Telecomp while awarding marks care was taken to exclude the open market projects and foreign exchange from the evaluation process.

100. As regards Skycell they had projected their operation in Madras for initial years which would be below profitable levels. Therefore, no dividend would have been paid to their foreign collaborators participating in the equity of company. The foreign exchange inflow position in their case was considered to be better. The markings came to be awarded on the same basis as in the case of all the bidders. The foreign collaborators of Skycell, BPL Systems and Projects, Usha Martin, Bharati Cellular and Tata Cellular specifically undertook to cover the foreign exchange funding by equity and loans. International roaming has been correctly taken into consideration. As submitted by the learned Solicitor General roaming is defined in paragraph 1.3.1.2of NIT as follows :

"Roaming. This feature shall enable a subscriber to communicate in cellular system other than its home registered one."

Paragraph 1.3.1.18 talks of home location registered. Paragraph 1.3.1.19 deals with Visitor Location Register (VLR) which says as follows :

"Visitor Location Register (VLR). VLR shall be able to store the following information. Their functions shall also include data retrieval, data collection, update of data entry, once PLMNs are established.

All these paragraphs will clearly establish that the system provides for facility of roaming to visitors. International roaming in GSM is well-accepted technique.

101. GSM is defined as a Global System for Mobile communications. The GSM specifications are highly standardised. This means that the systems that are designed as per GSM specifications will be compatible with each other and, therefore, can be easily connected together from day one.

102.Roaming in GSM cellular mobile systems means that a subscriber belonging to one operator can use his telephone to receive and make calls while he is in the area of another operator automatically. When a subscriber goes into the area of another operator, who has a roaming agreement with his another operator, the details of the subscriber available in the HLR (Home Location Register) of the home MSC (Mobile Switching Centre) are obtained by the visitor MSC and placed in the VLR (Visitor Location Register). The subscriber can originate and receive calls without feeling any difference. The roaming can be easily extended internationally and is already being done in parts of Europe. Since the systems are compatible, all that is required is an agreement between the operators for revenue sharing etc.

103.Thus, we find the argument that paragraph 2.4.7, namely, the financial projection of the proposed Cellular Mobile Cellular and the 7th criterion having been left out of consideration cannot be accepted.

3. Bias of Mr Nair Whether affects the selection?

104.In Black's Law Dictionary, 6th Edn. at page 162, bias is defined as under :

" Inclination; bent; prepossession; a preconceived opinion; a predisposition to decide a cause or an issue in a certain way, which does not leave the mind perfectly open to conviction. To incline to one side. Condition of mind, which sways judgment and renders judge unable to exercise his functions impartially in particular case. As used in law regarding disqualification of judge, refers to mental attitude or disposition of the judge toward a party to the litigation, and not to any views that he may entertain regarding the subject-matter involved. State ex rel Mitchell v. Sage Stores Co. 52"

The rule of bias is founded on the well-known maxim nemo debet esse judex in propria causa : no person can be a judge in his own cause.

105. de Smith's Constitutional and Administrative Law, New Edn., at p. 583, states as follows :

"First, an adjudicator must not have any direct financial or proprietary interest in the outcome of the proceedings. Secondly, he must not be reasonably suspected, or show a real likelihood, of bias."

106.In the instant case, the first aspect of the matter does not arise. As' regards the second, the law is as stated by de Smith's Constitutional and Administrative Law, New Edn., at pp. 584-85 "If an adjudicator is likely to be biased he is also disqualified from acting. Likelihood of bias may arise from a number of causes membership of an organisation or authority that is a party to the proceedings;

partisanship expressed in extra judicial pronouncements; the fact of appearing as a witness for a party to the proceedings; personal animosity or friendship towards a party; family relationship with a party; professional or commercial relationships with a party; and so on. The categories o f situations potentially giving rise to a likelihood of bias are not closed.

How should the test of disqualification for likelihood of bias be formulated?... A more common formulation of the test is : Would a member of the public, looking at the situation as a whole, reasonably suspect that a member of the adjudicating body would be biased? Another common formulation is : Is there in fact a real likelihood of bias? There is no need, on either formulation, to prove actual bias; indeed, the courts may refuse to entertain submissions designed to establish the actual bias of a member of an independent tribunal, on the ground that such an inquiry would be unseemly. In practice the test of ,reasonable suspicion' and 'real likelihood' of bias will generally lead to the same result. Seldom indeed will one find a situation in which reasonable persons adequately apprised of the facts will reasonably suspect bias but a court reviewing the facts will hold that there was no real likelihood of bias. Neither formulation is concerned wholly with appearances or wholly with objective reality. In ninety-nine cases out of a hundred it is enough for the court to ask itself whether a reasonable person viewing the facts would think that there was a substantial possibility of bias."

107. Geoffrey A. Flick in his work on Natural Justice Principles and Practical Application, 1979 Edn., at pp. 11 8-120, states 52 157 Kan 622, 143 P 2d 652, 655 "Personal Involvement : Whenever a decision- maker becomes personally involved with one of the parties there arises the suspicion that a determination may not be reached exclusively on the merits of the case as discussed at the hearing. Unlike allegations of bias by reason of the pecuniary interest of the decision- maker however, allegations of bias founded upon a personal involvement will only result in disqualification where there is a real likelihood that a hearing will not be fair. de Smith at pp. 232-37; David @ 12.02.

The most obvious group of cases calling for scrutiny are those in which one of the parties has close ties of kinship with the decision- maker. A chairman of county commissioners, therefore, cannot hear a petition to build a new road which was intended to pass over land belonging to his brother-in-law, nor can a member of a zoning commission determine his wife's application for a change in zoning from residential to business. Low v. Town of Madison53. In the last cited case the court was concerned with both the family sentiment that was present and with the opportunity for the wife to have what in reality a private hearing before the board with her husband acting as advocate. See p. 778. But not all family relationships will disqualify and, by way of contrast, on the circumstances of one particular case it was said that a board of adjustment could decide an application by a company for permission to develop a free parking area despite the fact that an employee of the company was the wife of one board member and the fact that a third or fourth cousin of another board member was the president of the company. Moody v. City of University Park54.

Disqualification on the basis of personal involvement is not, of course, limited to the above two situations but may result whenever there is a sufficient nexus between the decision-maker and a party to justify the appearance that this nexus may influence the decision reached: of R. v. Altrincham Justices, ex p Pennington55. Street, C.J. has stated the law in this respect in yet another New South Wales decision. Ex p Burnett, Re Wurth56. The last cited case involved a former officer of the Department of Education who later sat as a member of the Public Service Board inquiring into alleged false and scandalous allegations made by a teacher against various persons, including the officer in question, and during the course of his judgment Street, C.J. observed :

'Where bias arises not from (pecuniary) interest, the officer must have so conducted himself that a high probability arises of a bias inconsistent with the fair performance of his duties, with the result 53 60 A 2d 774 (Coun 1948) 54 278 SW 2d 912 (CT Civ App Tex 1955) 55 (1975) 1 QB 549: (1975) 2 All ER 78: (1975) 2 WLR 450 56 (1955) 72 WN (NSW) 457 that a substantial distrust of the result must exist in the minds of reasonable persons.' Put in other words, the issue is not merely whether justice has in fact been done, but whether it has manifestly and undoubtedly been seen to be done. It may, therefore, be improper for the clerk of the court to act as a solicitor for a party. Similarly, it may be unwise for a headmaster to sit in judgment upon a case involving a former pupil who had been adversely criticised in a detailed staff report signed by the headmaster some three months previously even where the existence of the report has been forgotten. R. v. Abingdon Justices, ex p CousinS57."

108.The leading cases on bias may now be seen. In R. v. Camborne Justices,ex p Pearce58 it was held : (All ER p.

855) "In R. v. Essex Justices ex p PerkinS21 Avory, J., said 'We have here to determine, however, whether or not there might appear to be a reasonable likelihood of his being biased.' And Swift, J., said (ibid., 490) :

'It is essential that justice should be so administered as to satisfy reasonable persons that the tribunal is impartial and unbiased.

As Lord Hewart, C.J., said in R. v. Sussex JJ., ex p McCarthy59 : "Nothing is to be done which creates even a suspicion that there has been an improper interference with the course of justice." Might a reasonable man suppose that there had here been such an interference with the course of justice?' In R. v. Salford Assessment Committee, ex p Ogden6O, Slesser, L.J. and Luxmoore, J. (ibid., 108) applied the 'reasonable likelihood' test, while Greene, L.J. (ibid.,

107) dissented only on the inference to be drawn from the facts. In Cottle v. Cottle61 Sir Boyd Merriman, P. asked himself the question whether the party complaining 'might reasonably have formed the impression that Mr Browning (the Chairman of the Bench) could not give this case an unbiased hearing.' Bucknill, J., said (ibid.) 'The test which we have to apply is whether or not a reasonable man, in all the circumstances, might suppose that there was an improper interference with the course of justice....' In the judgment of this court the right test is that prescribed by Blackburn, J. in R. v. Rand62, namely, that to disqualify a person from acting in a judicial or quasi- judicial capacity on the ground of interest 57 (1964) 108 Sol Jo 840 58 (1954) 2 All ER 850: (1955) 1 QB 41: (1954) 3 WLR 415 59 (1924) 1 KB 256: 1923 All ER Rep 233 60 (1937) 2 All ER 98: (1937) 2 KB 1 61 (1939) 2 All ER 535 62 (1866) 1 QB 230 (other than pecuniary or proprietary) in the subject-matter of the proceeding, a real likelihood of bias must be shown. This court is, further, of opinion that a real likelihood of bias must be made to appear not only from the materials in fact ascertained by the party complaining, but from such further facts as he might readily have ascertained and easily verified in the course of his inquiries. In the present case, for example, the facts relied on in the applicant's statement, under R.S.C., Ord. 59, R. 3(2), of the grounds of his application might create a more sinister impression than the full facts as found by this court, all or most of which would have been available to the applicant had he pursued his inquiries on learning that Mr Thomas was a member of the Cornwall County Council, and none of these further facts was disputed at the hearing of this motion. The frequency with which allegations of bias have come before the courts in recent times seems to indicate that the reminder of Lord Hewart, C.J., in R. v. Sussex JJ., ex p McCarthy59 that it is of fundamental importance that justice should not only be done, but should manifestly and undoubtedly be seen to be done' is being urged as a warrant for quashing convictions or invalidating orders on quite unsubstantial grounds and, indeed in some cases, on the flimsiest pretexts of bias."

In Metropolitan Properties Co. (FG.C.) Ltd. v. Lannon4 it was held thus (All ER p. 3 1 0) "... in considering whether there was a real likelihood of bias, the court does not look at the mind of the justice himself or at the mind of the chairman of the tribunal, or whoever it may be, who sits in a judicial capacity. It does not look to see if there was a real likelihood that he would, or did, in fact favour one side at the expense of the other. The court looks at the impression which would be given to other people. Even if he was as impartial as could be, nevertheless, if right- minded persons would think that, in the circumstances, there was a real likelihood of bias on his part, then he should not sit. And if he does sit, his decision cannot stand. See R. v. Huggins63; R. v. Sunderland Justices64, per Vaughan Williams, L.J. Nevertheless, there must appear to be a real likelihood of bias. Surmise or conjecture is not enough. See R. v. Camborne Justices, ex p Pearce58; R. v. Nailsworth Licensing Justices, ex p Bird65. There must be circumstances from which a reasonable man would think it likely or probable that the justice, or chairman, as the case may be, would, or did, favour one side unfairly at the expense of the other. The court will not enquire whether he did, in fact, favour one side unfairly. Suffice it that reasonable people might think he did. The reason is plain enough. Justice must be rooted in 63 (1895-99) All ER Rep 914: (1895) 1 QB 563 64 (1901) 2 KB 357 65 (1953) 2 All ER 652: (1953) 1 WLR 1046 confidence; and confidence is destroyed when right-minded people go away thinking: 'The judge was biased.' "

In R. v. Liverpool City Justices, ex p Topping66 it was observed : (All ER p. 494) "In the past there has also been a conflict of view as to the way in which that test should be applied. Must there appear to be a real likelihood of bias? Or is it enough if there appears to be a reasonable suspicion of bias? (For a discussion on the cases, see de Smith's Judicial Review of Administrative Action (4th Edn., 1980) pp. 262-264 and H.W.R. Wade, Administrative Law (5th Edn., 1982) pp. 430-

432.) We accept the view of Cross, L.J., expressed in Hannam v. Bradford City Council67, that there is really little, if any, difference between the two tests : ,If a reasonable person who has no knowledge of the matter beyond knowledge of the relationship which subsists between some members of the tribunal and one of the parties would think that there might well be bias, then there is in his opinion a real likelihood of bias. Of course, someone else with inside knowledge of the character of the members in question might say : "Although things don't look very well, in fact there is no real likelihood of bias." But that would be beside the point, because the question is not whether the tribunal will in fact be biased, but whether a reasonable man with no inside knowledge might well think that it might be biased.' We conclude that the test to be applied can conveniently be expressed by slightly adapting in words of Lord Widgery, C.J. in a test which he laid down in R. v. Uxbridge Justices, ex p Burbridge68 and referred to by him in R. v. McLean, ex p Aikens69: would a reasonable and fair-minded person sitting in court and knowing all the relevant facts have a reasonable suspicion that a fair trial for the applicant was not possible?"

In University College of Swansea v. Cornelius70 holds "Cases of bias and ostensible bias had to be regarded in the light of their own circumstances. The circumstances of this case could have no relevance to other cases."

109.The Indian Law can be gathered from the following rulings. In Manak Lal v. Dr Prem Chandl it was held thus: (SCR p. 58 1) "But where pecuniary interest is not attributed but instead a bias is suggested, it often becomes necessary to consider whether there is a reasonable ground for assuming the possibility of bias and whether it is 66 (1983) 1 All ER 490,494 67 (1970) 2 All ER 690, 700: (1970) 1 WLR 937, 949 68 (1972) Times, 21 June 69 (1974) 139 JP 261, 266 70 1988 ICR 735, 739 likely to produce in the minds of the litigant or the public at large a reasonable doubt about the fairness of the administration of justice. It would always be a question of fact to be decided in each case. 'The principle', says Halsbury, 'nemo debet esse judex in causa propria sua precludes a justice, who is interested in the subject- matter of a dispute, from acting as a justice therein'. In our opinion, there is and can be no doubt about the validity of this principle and we are prepared to assume that this principle applies not only to the justices as mentioned by Halsbury but to all tribunals and bodies which are given jurisdiction to determine judicially the rights of parties." In J. Mohapatra & Co. v. State of Orissa2 it was observed thus : (SCR p. 334: SCC p. 112, para 11) "It is no answer say that an author-member is only one of the members of the Assessment Sub- Committee and that the ultimate decision rests with the State Government which may reject any book out of the list of approved books. A similar argument was rejected by this Court in Kraipak case71. The State Government would normally be guided by the list approved by the Assessment Sub-Committee. Further, to say that such author-member is only one of the members of the Assessment Sub-Committee is to overlook the fact that the author member can subtly influence the minds of the other members against selecting books by other authors in preference to his own. It can also be that books by some of the other members ma y also have been submitted for selection and there can be between them a quid pro quo or, in other words, you see that my book is selected and in return I will do the same for you. In either case, when a book of an author-member comes up for consideration, the other members would feel themselves embarrassed in frankly discussing its merits. Such author-member may also be a person holding a high official position whom the other members may not want to displease. It can be that the other members may not be influenced by the fact that the book which they are considering for approval was written by one of their members. Whether they were so influenced or not is, however, a matter impossible to determine. It is not, therefore, the actual bias in favour of the author-member that is material but the possibility of such bias. All these considerations require that an author-member should not be a member of any such committee or subcommittee."

In Ashok Kumar Yadav v. State of Haryana3 this Court emphasised the reasonable likelihood of bias thus : (SCC p. 441, para 16) "This Court emphasised that it was not necessary to establish bias but it was sufficient to invalidate the selection process if it could be shown that there was reasonable likelihood of bias. The likelihood of bias may arise on account of proprietary interest or on account of personal reasons, such as, hostility to one party or personal friendship or 71 A. K. Kraipak v. Union of India, (1969) 2 SCC 262 family relationship with the other. Where reasonable likelihood of bias is alleged on the ground of relationship, the question would always be as to how close is the degree of relationship or in other words, is the nearness of relationship so great as to give rise to reasonable apprehension of bias on the part of the authority making the selection."

In Ranjit Thakur v. Union of India15 the law was stated by one of us, Venkatachaliah, J. (as he then was) as under : (SCR p. 520: SCC p. 618, para 17) "As to the tests of the likelihood of bias what is relevant is the reasonableness of the apprehension in that regard in the mind of the party. The proper approach for the judge is not to look at his own mind and ask himself, however, honestly, 'Am I biased?'; but to look at the mind of the party before him."

Reference was made therein to a dictum laid down by Justice Frankfurter in Public Utilities Commission of the District of Columbia v. Pollak72 which is reproduced as under: "The judicial process demands that a judge move within the framework of relevant legal rules and the covenanted modes of thought for ascertaining them. He must think dispassionately and submerge private feeling on every aspect of a case. There is a good deal of shallow talk that the judicial robe does not change the man within it. It does. The fact is that on the whole judges do lay aside private views in discharging their judicial functions. This is achieved through training, professional habits, self- discipline and that fortunate alchemy by which men are loyal to the obligation with which they are entrusted. But it is also true that reason cannot control the subconscious influence of feelings of which it is unaware. When there is ground for believing that such unconscious feelings may operate in the ultimate judgment, or may not unfairly lead others to believe they are operating, judges rescue themselves. They do not sit in judgment." In International Airports Authority of India v. K.D. Bali73 this Court observed thus : (SCC p. 367, para 5) "Several points were taken in support of the application for revocation. It was sought to be urged that the petitioner had lost confidence in the sole arbitrator and was apprehensive that the arbitrator was biased against the petitioner. It is necessary to reiterate before proceeding further what are the parameters by which an appointed arbitrator on the application of a party can be removed. It is well settled that there must be purity in the administration of justice as well as in administration of quasi- justice as are involved in the adjudicatory process before the arbitrators. It is well said that once the arbitrator enters in an arbitration, the arbitrator must not be guilty of any act which can possibly be construed as indicative of partiality or unfairness. It is 72 343 US 451, 466: 96 L Ed 1068 (1961) 73 (1988) 2 SCC 360, 367 not a question of the effect which misconduct on his part had in fact upon the result of the proceeding, but of what effect it might possibly have produced. It is not enough to show that, even if there was misconduct on his part, the award was unaffected by it, and was in reality just; arbitrator must not do anything which is not in itself fair and impartial. See Russel on Arbitration, 18th Edn., p. 378 and observations of Justice Boyd in Brien and Brien, Re74. Lord O'Brien in King (De Vosci) v. Justice of Queen's Country75 observed as follows :

'By bias I understand a real likelihood of an operative prejudice, whether conscious or unconscious. There must in my opinion be reasonable evidence to satisfy us that there was a real likelihood of bias. I do not think that their vague suspicions of whimsical, capricious and unreasonable people should be made a standard to regulate our action here. It might be a different matter if suspicion rested on reasonable grounds was reasonably generated but certainly mere flimsy, elusive, morbid suspicions should not be permitted to form a ground of decision."' (emphasis supplied) In Union Carbide Corpn. v. Union of India76 this Court observed thus (SCC p. 667, para 161) "But the effects and consequences of non- compliance may alter with situational variations and particularities, illustrating a 'flexible use of discretionary remedies to meet novel legal situations'. 'One motive' says Prof. Wade 'for holding administrative acts to be voidable where according to principle they are void may be a desire to extend the discretionary powers of the Court'. As observed by Lord Reid in Wiseman v.

Borneman77 natural justice should not degenerate into a set of hard and fast rules. There should be a circumstantial flexibility."

110. In the light of this let us find out whether bias has been established? The Report of the Tender Evaluation Committee was made on 16-5-1992. In that Committee Mr B.R. Nair was a party. As seen above, the offer of the four companies did not fully satisfy the criteria. Their cases were recommended to be considered for condonation. The four companies are

1. BPL Systems and Projects,

2. Mobile Communication India Private Limited,

3. Mobile Telecom Services Limited, and

4. Indian Telecom Private Limited.

Mr B.R. Nair, Member (Production) made the following note: "I agree with the recommendations of the Evaluation Committee that the four firms must be in paragraph 3 of page 1/N should be included in 74 (1910) 2 IR 84 75 (1908) 2 IR 285 76 (1991) 4 SCC 584, 667 77 1971 AC 297: (1969) 3 All ER 275: (1969) 3 WLR 706 the short-list. Thus, there would be 14 companies in the short-list instead of 16 recommended by Adviser (0)."

111. On 8-9-1992, Mr Nair, as Member of the Committee, agreed to a noting that only three companies, Bharati Cellular, BPL Systems and Projects and Skycell qualified for selection. After further discussion, 8 companies came to be selected and the note was accordingly put up on 9-10-1992. This recommendation is agreed to by Mr Nair.

112. According to Mr Harish Salve, the very presence of Mr Nair itself will amount to bias.

113.In this case, as noted above, the crucial test is whether there was a real likelihood of bias. As to how Mr R. Satish Kumar, the son of Mr B.R, Nair, came to be appointed in BPL Systems and Projects is explained in the additional affidavit filed on behalf of BPL Systems & Projects Ltd., Respondent 10, by Mr S. Sunder Rao, Corporate Personnel Manager of BPL Group of Companies, including Respondent 10-Company. The relevant portion is extracted as under :

"With regard to the selection and appointment of Shri R. Satish Kumar, I state as follows :

That Respondent 10 Company desired to employ certain managers and executives as follows :

(i) Sr, Manager, (Push Button Telephone) for New Delhi, Bangalore and Bombay.

(ii)Manager (Communications) for Madras, Calcutta and Bangalore.

(iii)Territory Manager (Sales) for Delhi, Hyderabad and Madras.

(iv)Sales Executives for Delhi, Madras, Kanpur, Chandigarh, Baroda, Kochi, Calcutta, Bhopal, Pune and Coimbatore. These posts were advertised for in several newspapers as follows

(i) The Times of India, Delhi and Bombay Edns.

(ii)The Hindustan Times, Delhi Edn.

(iii)Statesman, Calcutta Edn.

(iv)The Hindu, All India Edn.

(v) Deccan Herald, Bangalore.

These advertisements appeared between 26-8-1991 and 29-8- 1991. The eligibility conditions for the candidates was specified and with regard to the post of Territory Manager (Sales) it was mentioned that the candidates should be an Electronics/Electrical Engineer with 5/6 years' experience of office automation products, Computer, Telecom equipments, etc.

In response to advertisement Shri R. Satish Kumar applied for the post of Territory Manager (Sales) vide his letter dated 28-8-1991 enclosing thereby his bio-data.

As per practice of the Respondent-Company the bio-data of all the applicants were scrutinised by the Personnel Department and thereafter by the Assistant General Manager of the Respondent-Company. Thereafter the short- listed candidates were called for interview on various dates. Shri Satish Kumar was called for an interview on 6-9 1991. Two other candidates were also interviewed for this post. Shri Satish Kumar was interviewed by the Senior Officer of the company including myself. At the conclusion of the interview as per practice, an internal assessment form was filled by the interviewers.

On the basis of the said interview Shri Satish Kumar was selected and a letter dated 21-10- 1991 was addressed to him offering him the said post. Shri Satish Kumar was required to report for duty on or before 2-12-1991 at Bangalore. Shri Satish Kumar however requested for some time to enable him to handover the charge in his previous company and this was agreed to by the company. Shri Satish Kumar accordingly joined Respondent 10 on 6-1-1992.

I state and submit that Shri Satish Kumar was selected by Respondent 10-Company in the normal course and the selection was purely on merit."

It is to be seen that Mr Satish Nair is only one of the officers in BPL Systems and Projects, which has over 5500 employees in 27 offices all over India. There are 89 officers of his rank.

114.Mr B.R. Nair was not a decision-maker at all. He was one of the recommending authorities. As Director General of Communication as well as Telecom Authority his involvement in the approval and selection of tender was indispensable. He came to be appointed as Member (Services) on 29-5-1992. By virtue of the notification dated 28-7-1992 Mr B.R. Nair became the Director General of Telecommunication. As such, he could exercise all the powers under Section 3(6) of the Indian Telegraphs Act of 1885. Such a Telecom Authority has the right to grant cellular operating licences to the successful party and also reject any bids without assigning any reason. Registration fees, security deposit and other financial charges shall be fixed by the licenser in consultation with the Telecom Authority. This is what is stated in the financial bid. Therefore, Mr B.R. Nair could not dissociate himself from the decision-making process. It is under these circumstances the High Court rightly applied the doctrine of necessity. This Court in Charan Lal Sahu v. Union of India16 dealt with this doctrine which is stated as follows : (SCC p. 694, para 105) "The question whether there is scope for the Union of India being responsible or liable as joint tort-feasor is a difficult and different question. But even assuming that it was possible that the Central Government might be liable in a case of this nature, the learned Attorney General was right in contending that it was only proper that the Central Government should be able and authorised to represent the victims. In such a situation, there will be no scope of the violation of the principles of natural justice. The doctrine of necessity would be applicable in a situation of this nature. The doctrine has been elaborated, in Halsbury's Laws of England, 4th Edn., p. 89, paragraph 73, where it was reiterated that even if all the members of the Tribunal competent to determine a matter were subject to disqualification, they might be authorised and obliged to hear that matter by virtue of the operation of the common law doctrine of necessity. An adjudicator who is subject to disqualification on the ground of bias or interest in the matter which he has to decide may in certain circumstances be required to adjudicate if there is no other person who is competent or authorised to be adjudicator or if a quorum cannot be formed without him or if no other competent tribunal can be constituted."

Therefore, we are unable to accept the contentions of Mr Soli J. Sorabjee and Mr Hafish Salve.

115.We hold Mr B.R. Nair's involvement did not vitiate the selection on the ground of bias. Since we have reached this conclusion we are not going to the other questions argued by Mr F.S. Nariman whether India Telecomp or Tata Cellular could urge this point relating to bias.

4. Whether the Apex Committee has been bypassed?

116.After finding that only three companies qualified for selection on 8-9-1992 the following note was made by Mr G.T. Narayanan, Adviser (Operations) :

"The financial bid which was approved by the apex committee was given to the short-listed bidders and these were received and opened on 17-8-1992. These were evaluated by the Tender Evaluation Committee (TEC). The evaluation report is placed below. The financial evaluation was done based upon the weightages of the various parameters namely, rental, financing, foreign exchange inflow/outflow, financial strength, experience and purchase plans. The rental was given the maximum weightage. The various guidelines made for giving the marks are at Annexure 1 (page 11, Flag 'A').

So far as the rental and other allied parameters are concerned, there are wide variations of rent, deposit, registration/connection fee. In some cases rent is zero. It was considered by the TEC that these are to be equated to one parameter as 'equated rental' and the method adopted was loading the basic rental and other charges like deposit, interest rate @ 13% per annum. Based upon these assumptions, the gradation for various bidders for each city is at page 9 of the main report.

The Chairman and Members of the Telecom Commission were consulted in this regard. It was felt that the rate of interest adopted by the TEC was low, and the maximum lending rate of the State Bank of India as on 1-8-1992 viz. 21.75% is more appropriate to adopt both for refundable and non-refundable deposits and nonreturnable charges. For the non-refundable charges the monthly a mortised value over 5 years at the lending rate, viz., 21.75% should be used for loading the rental, to get at the equivalent rental value which represents the actual monthly burden on the subscribers. As per this guideline, the TEC gave the fresh calculations on 7-9-1992 and a new gradation list was prepared which is placed at Flag 'B'.

After examining the TEC report the following points have come to light-

(i) M/s Hutchison Max India Ltd. in their bid document (Annexure D) have not given proper and full compliance. The TEC has observed : 'Compliance to Chapter III (Operative Conditions) and Chapter IV (Financial Conditions) has not been indicated by the bidder.' Thus, it clearly shows that they have not complied with these important conditions which form the very basis of the financial bid. It is evident that the bidder has serious reservations about financial conditions and operative conditions and if granted a licence, there is a possibility of litigation.

(ii)Since we require good operators with experience the minimum of 10 marks out of 15 for this parameter is considered a must and those bidders who have scored less than 10 for this parameter should be disqualified. This represents an experience of handling of 1 lakh cellular phones or 80,000 with a GSM licence.

(iii)In accordance with the policy of the Government for encouraging foreign exchange investment only those who do foresee the inflow of foreign exchange should be considered. For this parameter the TEC had allocated 5 marks to those bids which were foreign exchange neutral. Those getting more than 5 indicate a net foreign exchange inflow. Thus, 5 marks or above for this parameter is considered essential and those getting below 5 marks deserve to be disqualified.

So with the points listed above taken into account, the following companies qualify city-wise as per the gradation- Delhi

1. Bharati Cellular

2. BPL Systems & Projects Ltd.

3. Sterling Cellular

4. Tata Cellular Calcutta

1. Bharati Cellular

2. Sterling Cellular

3. Tata Cellular (on an exclusive basis) Bombay

1. Bharati Cellular

2. BPL Systems & Projects Ltd.

3. Sterling Cellular

4. Tata Cellular Madras

1. Bharati Cellular

2. Sterling Cellular

4. Tata Cellular (on an exclusive basis) While making the final selection, it should be borne in mind that Sterling Cellular has got a problem which is explained in the notes of DDG (Vig.) placed below. Sterling Computer which is mentioned in the notes of DDG (Vig.) flag 'C' has a tie-up with Sterling Cellular from the list of approved operators.

Summarizing, the following operators are recommended for giving the cellular licence-

------------------------------------------------------------

-----------------------------------------------------------

Bombay

1. Bharati Cellular 37.3 7 1578.3 SFR France

2. BPL Systems & 33.2 6 1476.2France Projects Ltd. Telecom Delhi

1. Bharati 41.0 8 1583.0SFR France Cellular

2. BPL Systems 33.8 6 1476.8 France & Projects Ltd. Telecom Madras

1. Bharati 38.5 8 1580.0SFR France Cellular

2. Skycell 24.6 10 1571.6 Bell South Calcutta

1. Bharati Cellular 27.1 8 1569.1 SFR France There is no other bidder who qualifies for giving the licence. Even though Tata Cellular fulfils all the conditions but in bid document they have based their calculations on single operator concept. However, we may, if approved by Telecom Commission and High-Power Committee, make a counter-offer to operate on a non-exclusive basis. After the operators are selected, tariff fixation and other licensing terms can be negotiated by the Telecom authorities.

A separate note is being prepared for sending to the High- Power Committee based upon the observations that are likely to be made on this note.

For approval, please.

Member (Services) Member (Production) Member (Finance) Chairman (TC) sd/-

(G.T. Narayanan) Adviser (Operations) 8-9-1992 The proposal on pre-page with all the relevant calculation sheets and TEC report, copy of the F.B. document, may please be sent to the HighPower Committee nominated by NOS (C) for its consideration and for making final recommendations to the Government Re selection of the licensees. sd/ 10-9-1992 Adv. (0) out of stn.

DDG (TM) A brief note, copies of TEC report, financial tender document have been sent to the High-Power Committee. The note was shown to Member (S) before dispatch.

(emphasis supplied) sd/ 10-9-1992 Adv. (O) sd/-

G.T Narayanan 14-9-1992"

117.On 10-9-1992 the Chairman (TC) made the following note: "In pursuance of the orders of the MOS (C), a Committee consisting of Principal Secretary to the Prime Minister, in his capacity as Chairman, Foreign Investment Promotion Board, Secretary Finance, Secretary Electronics and Chairman Telecom Commission was appointed to make recommendations regarding selection of the franchisees to provide Cellular Mobile Telephone Service in the four metro cities. This Committee examined the bids received against the tenders floated on the basis of Tender Evaluation Committee report and made recommendations to MOS (C) regarding short-listing of the bidders and the financial bids document. The financial bids from the short-listed bidders have now been received and examined in the Department. The recommendations of the Evaluation Committee are being forwarded to the members of the High-Level Committee appointed by MOS (C) for examination and making recommendations to the Government regarding final selection of the franchisees.

I spoke to Principal Secretary to the Hon'ble Prime Minister with the request to expedite the process. He indicated that the Committee earlier appointed by MOS (C) stands dissolved and a fresh Committee will have to be nominated,for considering the financial bids etc. He also indicated that he proposes to put up the case to the Hon'ble Prime Minister for his clearance. It is, therefore, proposed to issue a letter to the members of the High-Level Committee as per draft placed below. The same may please be seen by MOS (C) for approval before issue.

In the draft letter it has been indicated that the same Committee will also examine the bids received for provision of the Paging Service in 27 cities first for short-listing and finalising the financial bids and later for selection of the franchisees. The documents relating to short-listing of Paging Service bidders have also been sent separately to the members of the Committee.

sd/-

(H.R Wagle) Chairman (TC) 10-9-1992 Mos (C) 11-9-1992 D.O. to Principal Secretary with copies to ES./Electronics Secretary may issue sd/ PS. - D.O. issued pl. sd/14-9 DDG(TM)"

However, the D.O. came to be issued in accordance with the note of 10-9-1992 dissolving the apex committee. Therefore, it is not correct to contend, as urged by Mr Harish Salve, that the apex committee had been bypassed. The learned Solicitor General is right in his submission.

5. Entry of Hidden Criteria - Whether valid?

118. In the original tender document, paragraph 2.2.1 in relation to the Subscriber's Capacity states as follows : "Subscriber Capacity: 1000 with modular expansion up to minimum 40,000 subscribers."

In Section 11 of General Condition, clause 1(d) states "Copy of the agreement between the Indian and the foreign partner, if any foreign partner is proposed." Chapter 11 of General Conditions in paragraph 2.4.5 states "Experience of the Foreign operating partner;" On 8-9-1992 Mr G.T. Narayanan, Adviser (Operations) in his note in the file inter alia stated as follows :"""
date_indicators="([\s0-3][0-9][\/-][01][0-9][/\-][12][09][0-9][0-9]|[\s0-3][0-9][\/-][01][0-9][/\-][0-9][0-9]|[\s0-3][0-9](((rd)|(st)|(nd)|(th))?)(\s?)((January)|(JAN)|(February)|(FEB)|(March)|(MAR)|(April)|(apr)|(May)|(June)|(Jun)|(July)|(jul)|(August)|(Aug)|(September)|(Sept)|(October)|(OCT)|(November)|(NOVEMBER)|(NOV)|(Nov)|(nov)|(December)|(DEC))(,?)(\s?)[12][90][0-9][0-9]|((January)|(JAN)|(February)|(FEB)|(March)|(MAR)|(April)|(apr)|(May)|(June)|(Jun)|(July)|(jul)|(August)|(Aug)|(September)|(Sept)|(October)|(OCT)|(November)|(nov)|(December)|(DEC))(\s)(\s?)[0-3][0-9](,?)(\s?)[12][90][0-9][0-9])"  
judgment_date_indicators = "((Judgment)|(Judgement)|(Reserved)|(bench)|(date of judgement)|(Case No.)|(Case number)|(Petitoner)(s?)|(Respondent)(s?))"
non_judgement_date_indicators="(since)"


case_date={"date":"","score":-1}
date = re.finditer(date_indicators,text,re.IGNORECASE)
# for i in date:
#     print(i.group())
doc_nlp = nlp(text)
for sent in doc_nlp.sents:
        
        
        
        for count,m in enumerate(re.finditer(date_indicators, sent.text, re.IGNORECASE)):
            print("Date Sentence :" + sent.text)
            score = 0
            for j in re.finditer(judgment_date_indicators,sent.text, re.IGNORECASE):
                score = score +1
                
            for k in re.finditer(non_judgement_date_indicators,sent.text, re.IGNORECASE):
                score = score -1
            print(score)

            if (case_date["score"]<score):
                case_date["date"] = m.group()
                case_date["score"]=score
                print("reassign date :" + str(m.group()))
print(case_date["date"])    

