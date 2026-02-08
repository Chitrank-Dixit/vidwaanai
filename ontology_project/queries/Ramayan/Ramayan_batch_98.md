# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Ramayan 0.1941)
- **Original**: Credits March 18, 2008 Project Gutenberg TEI edition 1 Produced by Juliet Sutherland, John Bruno Hare, David King, and the Online Distributed Proofreading Team at <http://www.pgdp.net/>. Page-images available at <http://www.pgdp.net/projects/projectID3e283e798085a/>
- **Translation**: 

---

### Verse 2 (Ramayan 0.1942)
- **Original**: A Word from Project Gutenberg This file should be named 24869-pdf.pdf or 24869-pdf.zip. This and all associated files of various formats will be found in: http://www.gutenberg.org/dirs/2/4/8/6/24869/ Updated editions will replace the previous one— the old editions will be renamed. Creating the works from public domain print editions means that no one owns a United States copyright in these works, so the Foundation (and you!) can copy and distribute it in the United States without permission and without paying copyright royalties. Special rules, set forth in the General Terms of Use part of this license, apply to copying and distributing Project Gutenberg™ electronic works to protect the Project Gutenberg™ concept and trademark. Project Gutenberg is a registered trademark, and may not be used if you charge for the eBooks, unless you receive specific permission. If you do not charge anything for copies of this eBook, complying with the rules is very easy. You may use this eBook for nearly any purpose such as creation of deriva- tive works, reports, performances and research. They may be modified and printed and given away— you may do practically anythingwith public domain eBooks. Redistribution is subject to the trademark license, especially commercial redistribution.
- **Translation**: 

---

### Verse 3 (Ramayan 0.1943)
- **Original**: The Full Project Gutenberg License Please read this before you distribute or use this work. To protect the Project Gutenberg™ mission of promoting the free distribution of electronic works, by using or distributing this work (or any other work associated in any way with the phrase “Project Gutenberg”), you agree to comply with all the terms of the Full Project Gutenberg™ License (available with this file or online at http://www.gutenberg.org/license). Section 1. General Terms of Use & Redistributing Project Gutenberg™ electronic works 1.A. By reading or using any part of this Project Gutenberg™ elec- tronic work, you indicate that you have read, understand, agree to and accept all the terms of this license and intellectual property (trademark/copyright) agreement. If you do not agree to abide by all the terms of this agreement, you must cease using and return or destroy all copies of Project Gutenberg™ electronic works in your possession. If you paid a fee for obtaining a copy of or access to a Project Gutenberg™ electronic work and you do not agree to be bound by the terms of this agreement, you may obtain a refund from the person or entity to whom you paid the fee as set forth in paragraph 1.E.8.
- **Translation**: 

---

### Verse 4 (Ramayan 0.1944)
- **Original**: The Full Project Gutenberg License 1929 1.B. “Project Gutenberg” is a registered trademark. It may only be used on or associated in any way with an electronic work by people who agree to be bound by the terms of this agreement. There are a few things that you can do with most Project Guten- berg™ electronic works even without complying with the full terms of this agreement. See paragraph 1.C below. There are a lot of things you can do with Project Gutenberg™ electronic works if you follow the terms of this agreement and help preserve free future access to Project Gutenberg™ electronic works. See paragraph 1.E below. 1.C. The Project Gutenberg Literary Archive Foundation (“the Foun- dation” or PGLAF), owns a compilation copyright in the col- lection of Project Gutenberg™ electronic works. Nearly all the individual works in the collection are in the public domain in the United States. If an individual work is in the public domain in the United States and you are located in the United States, we do not claim a right to prevent you from copying, distributing, performing, displaying or creating derivative works based on the work as long as all references to Project Gutenberg are removed. Of course, we hope that you will support the Project Gutenberg™ mission of promoting free access to electronic works by freely sharing Project Gutenberg™ works in compliance with the terms of this agreement for keeping the Project Gutenberg™ name associated with the work. You can easily comply with the terms of this agreement by keeping this work in the same format with its attached full Project Gutenberg™ License when you share it without charge with others.
- **Translation**: 

---

### Verse 5 (Ramayan 0.1945)
- **Original**: 1930 The Ramayana 1.D. The copyright laws of the place where you are located also govern what you can do with this work. Copyright laws in most countries are in a constant state of change. If you are outside the United States, check the laws of your country in addition to the terms of this agreement before downloading, copying, displaying, performing, distributing or creating derivative works based on this work or any other Project Gutenberg™ work. The Foundation makes no representations concerning the copyright status of any work in any country outside the United States. 1.E. Unless you have removed all references to Project Gutenberg: 1.E.1. The following sentence, with active links to, or other immediate access to, the full Project Gutenberg™ License must appear prominently whenever any copy of a Project Gutenberg™ work (any work on which the phrase“Project Gutenberg” appears, or with which the phrase“Project Gutenberg” is associated) is accessed, displayed, performed, viewed, copied or distributed: This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at http://www.gutenberg.org 1.E.2.
- **Translation**: 

---

### Verse 6 (Ramayan 0.1946)
- **Original**: The Full Project Gutenberg License 1931 If an individual Project Gutenberg™ electronic work is derived from the public domain (does not contain a notice indicating that it is posted with permission of the copyright holder), the work can be copied and distributed to anyone in the United States without paying any fees or charges. If you are redistributing or providing access to a work with the phrase“Project Gutenberg” associated with or appearing on the work, you must comply either with the requirements of paragraphs 1.E.1 through 1.E.7 or obtain permission for the use of the work and the Project Gutenberg™ trademark as set forth in paragraphs 1.E.8 or 1.E.9. 1.E.3. If an individual Project Gutenberg™ electronic work is posted with the permission of the copyright holder, your use and dis- tribution must comply with both paragraphs 1.E.1 through 1.E.7 and any additional terms imposed by the copyright holder. Ad- ditional terms will be linked to the Project Gutenberg™ License for all works posted with the permission of the copyright holder found at the beginning of this work. 1.E.4. Do not unlink or detach or remove the full Project Gutenberg™ License terms from this work, or any files containing a part of this work or any other work associated with Project Gutenberg™ . 1.E.5. Do not copy, display, perform, distribute or redistribute this electronic work, or any part of this electronic work, without prominently displaying the sentence set forth in paragraph 1.E.1
- **Translation**: 

---

### Verse 7 (Ramayan 0.1947)
- **Original**: 1932 The Ramayana with active links or immediate access to the full terms of the Project Gutenberg™ License. 1.E.6. You may convert to and distribute this work in any binary, compressed, marked up, nonproprietary or proprietary form, in- cluding any word processing or hypertext form. However, if you provide access to or distribute copies of a Project Gutenberg™ work in a format other than“Plain Vanilla ASCII” or other format used in the official version posted on the official Project Gutenberg™ web site (http://www.gutenberg.org), you must, at no additional cost, fee or expense to the user, provide a copy, a means of exporting a copy, or a means of obtaining a copy upon request, of the work in its original“Plain Vanilla ASCII” or other form. Any alternate format must include the full Project Gutenberg™ License as specified in paragraph 1.E.1. 1.E.7. Do not charge a fee for access to, viewing, displaying, per- forming, copying or distributing any Project Gutenberg™ works unless you comply with paragraph 1.E.8 or 1.E.9. 1.E.8. You may charge a reasonable fee for copies of or providing access to or distributing Project Gutenberg™ electronic works provided that • You pay a royalty fee of 20% of the gross profits you derive from the use of Project Gutenberg™ works calculated using the method you already use to calculate your applicable tax- es. The fee is owed to the owner of the Project Gutenberg™
- **Translation**: 

---

### Verse 8 (Ramayan 0.1948)
- **Original**: The Full Project Gutenberg License 1933 trademark, but he has agreed to donate royalties under this paragraph to the Project Gutenberg Literary Archive Foun- dation. Royalty payments must be paid within 60 days following each date on which you prepare (or are legally required to prepare) your periodic tax returns. Royalty payments should be clearly marked as such and sent to the Project Gutenberg Literary Archive Foundation at the ad- dress specified in Section 4,“Information about donations to the Project Gutenberg Literary Archive Foundation.” You provide a full refund of any money paid by a user who notifies you in writing (or by e-mail) within 30 days of receipt that s/he does not agree to the terms of the full Project Gutenberg™ License. You must require such a user to return or destroy all copies of the works possessed in a physical medium and discontinue all use of and all access to other copies of Project Gutenberg™ works. You provide, in accordance with paragraph 1.F.3, a full refund of any money paid for a work or a replacement copy, if a defect in the electronic work is discovered and reported to you within 90 days of receipt of the work. You comply with all other terms of this agreement for free distribution of Project Gutenberg™ works. 1.E.9. If you wish to charge a fee or distribute a Project Gutenberg™ electronic work or group of works on different terms than are set forth in this agreement, you must obtain permission in writing from both the Project Gutenberg Literary Archive Foundation and Michael Hart, the owner of the Project Gutenberg™ trademark. Contact the Foundation as set forth in Section 3 below. 1.F.
- **Translation**: 

---

### Verse 9 (Ramayan 0.1949)
- **Original**: 1934 The Ramayana 1.F.1. Project Gutenberg volunteers and employees expend consider- able effort to identify, do copyright research on, transcribe and proofread public domain works in creating the Project Guten- berg™ collection. Despite these efforts, Project Gutenberg™ electronic works, and the medium on which they may be stored, may contain“Defects,” such as, but not limited to, incomplete, inaccurate or corrupt data, transcription errors, a copyright or other intellectual property infringement, a defective or damaged disk or other medium, a computer virus, or computer codes that damage or cannot be read by your equipment. 1.F.2. LIMITED WARRANTY, DISCLAIMER OF DAMAGES — Except for the“Right of Replacement or Refund” described in paragraph 1.F.3, the Project Gutenberg Literary Archive Foun- dation, the owner of the Project Gutenberg™ trademark, and any other party distributing a Project Gutenberg™ electronic work under this agreement, disclaim all liability to you for damages, costs and expenses, including legal fees. YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE PROVIDED IN PARAGRAPH F3. YOU AGREE THAT THE FOUNDATION, THE TRADE- MARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE LIABLE TO YOU FOR AC- TUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH DAMAGE. 1.F.3.
- **Translation**: 

---

### Verse 10 (Ramayan 0.1950)
- **Original**: The Full Project Gutenberg License 1935 LIMITED RIGHT OF REPLACEMENT OR REFUND — If you discover a defect in this electronic work within 90 days of receiving it, you can receive a refund of the money (if any) you paid for it by sending a written explanation to the person you received the work from. If you received the work on a physical medium, you must return the medium with your written explanation. The person or entity that provided you with the defective work may elect to provide a replacement copy in lieu of a refund. If you received the work electronically, the person or entity providing it to you may choose to give you a second opportunity to receive the work electronically in lieu of a refund. If the second copy is also defective, you may demand a refund in writing without further opportunities to fix the problem. 1.F.4. Except for the limited right of replacement or refund set forth in paragraph 1.F.3, this work is provided to you 'AS-IS,' WITH NO OTHER WARRANTIES OF ANY KIND, EXPRESS OR IM- PLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTIBILITY OR FITNESS FOR ANY PURPOSE. 1.F.5. Some states do not allow disclaimers of certain implied war- ranties or the exclusion or limitation of certain types of damages. If any disclaimer or limitation set forth in this agreement violates the law of the state applicable to this agreement, the agreement shall be interpreted to make the maximum disclaimer or limi- tation permitted by the applicable state law. The invalidity or unenforceability of any provision of this agreement shall not void the remaining provisions.
- **Translation**: 

---

### Verse 11 (Ramayan 0.1951)
- **Original**: 1936 The Ramayana 1.F.6. INDEMNITY — You agree to indemnify and hold the Foun- dation, the trademark owner, any agent or employee of the Foundation, anyone providing copies of Project Gutenberg™ electronic works in accordance with this agreement, and any volunteers associated with the production, promotion and distri- bution of Project Gutenberg™ electronic works, harmless from all liability, costs and expenses, including legal fees, that arise directly or indirectly from any of the following which you do or cause to occur: (a) distribution of this or any Project Gutenberg™ work, (b) alteration, modification, or additions or deletions to any Project Gutenberg™ work, and (c) any Defect you cause. Section 2. Information about the Mission of Project Gutenberg™ Project Gutenberg™ is synonymous with the free distribution of electronic works in formats readable by the widest variety of computers including obsolete, old, middle-aged and new com- puters. It exists because of the efforts of hundreds of volunteers and donations from people in all walks of life. Volunteers and financial support to provide volunteers with the assistance they need, is critical to reaching Project Gutenberg™ 's goals and ensuring that the Project Gutenberg™ collection will remain freely available for generations to come. In 2001, the Project Gutenberg Literary Archive Foundation was created to provide a secure and permanent future for Project Gutenberg™
- **Translation**: 

---

### Verse 12 (Ramayan 0.1952)
- **Original**: The Full Project Gutenberg License 1937 and future generations. To learn more about the Project Guten- berg Literary Archive Foundation and how your efforts and donations can help, see Sections 3 and 4 and the Foundation web page at http://www.pglaf.org. Section 3. Information about the Project Gutenberg Literary Archive Foundation The Project Gutenberg Literary Archive Foundation is a non profit 501(c)(3) educational corporation organized under the laws of the state of Mississippi and granted tax exempt status by the Internal Revenue Service. The Foundation's EIN or federal tax identification number is 64-6221541. Its 501(c)(3) letter is posted at http://www.gutenberg.org/fundraising/pglaf. Contribu- tions to the Project Gutenberg Literary Archive Foundation are tax deductible to the full extent permitted by U.S. federal laws and your state's laws. The Foundation's principal office is located at 4557 Melan Dr. S. Fairbanks, AK, 99712., but its volunteers and employees are scattered throughout numerous locations. Its business office is located at 809 North 1500 West, Salt Lake City, UT 84116, (801) 596-1887, email business@pglaf.org. Email contact links and up to date contact information can be found at the Foundation's web site and official page at http://www.pglaf.org For additional contact information: Dr. Gregory B. Newby Chief Executive and Director gbnewby@pglaf.org
- **Translation**: 

---

### Verse 13 (Ramayan 0.1953)
- **Original**: 1938 The Ramayana Section 4. Information about Donations to the Project Gutenberg Literary Archive Foundation Project Gutenberg™ depends upon and cannot survive without wide spread public support and donations to carry out its mission of increasing the number of public domain and licensed works that can be freely distributed in machine readable form accessible by the widest array of equipment including outdated equipment. Many small donations ($1 to $5,000) are particularly important to maintaining tax exempt status with the IRS. The Foundation is committed to complying with the laws regulating charities and charitable donations in all 50 states of the United States. Compliance requirements are not uniform and it takes a considerable effort, much paperwork and many fees to meet and keep up with these requirements. We do not solicit donations in locations where we have not received writ- ten confirmation of compliance. To SEND DONATIONS or determine the status of compliance for any particular state visit http://www.gutenberg.org/fundraising/donate While we cannot and do not solicit contributions from states where we have not met the solicitation requirements, we know of no prohibition against accepting unsolicited donations from donors in such states who approach us with offers to donate. International donations are gratefully accepted, but we cannot make any statements concerning tax treatment of donations re- ceived from outside the United States. U.S. laws alone swamp our small staff. Please check the Project Gutenberg Web pages for current donation methods and addresses. Donations are accepted in a number of other ways including checks, online payments and
- **Translation**: 

---

### Verse 14 (Ramayan 0.1954)
- **Original**: The Full Project Gutenberg License 1939 credit card donations. To donate, please visit: http://www.guten- berg.org/fundraising/donate Section 5. General Information About Project Gutenberg™ electronic works. Professor Michael S. Hart is the originator of the Project Guten- berg™ concept of a library of electronic works that could be freely shared with anyone. For thirty years, he produced and dis- tributed Project Gutenberg™ eBooks with only a loose network of volunteer support. Project Gutenberg™ eBooks are often created from several printed editions, all of which are confirmed as Public Domain in the U.S. unless a copyright notice is included. Thus, we do not necessarily keep eBooks in compliance with any particular paper edition. Each eBook is in a subdirectory of the same number as the eBook's eBook number, often in several formats including plain vanilla ASCII, compressed (zipped), HTML and others. Correctededitionsof our eBooks replace the old file and take over the old filename and etext number. The replaced older file is renamed.Versionsbased on separate sources are treated as new eBooks receiving new filenames and etext numbers. Most people start at our Web site which has the main PG search facility: http://www.gutenberg.org
- **Translation**: 

---

### Verse 15 (Ramayan 0.1955)
- **Original**: 1940 The Ramayana This Web site includes information about Project Guten- berg™ , including how to make donations to the Project Guten- berg Literary Archive Foundation, how to help produce our new eBooks, and how to subscribe to our email newsletter to hear about new eBooks.
- **Translation**: 

---

### Verse 16 (Ramayana 0.1)
- **Original**: The Project Gutenberg EBook of The Ramayana This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at http://www.guten- berg.org/license Title: The Ramayana Release Date: March 18, 2008 [Ebook 24869] Language: English ***START OF THE PROJECT GUTENBERG EBOOK THE RAMAYANA***
- **Translation**: 

---

### Verse 17 (Ramayana 0.2)
- **Original**: The RÁMÁYAN of VÁLMÍKI Translated into English Verse by Ralph T. H. Griffith, M.A. Principal of the Benares College London: Trübner & Co. Benares: E. J. Lazarus and Co. 1870-1874
- **Translation**: 

---

### Verse 18 (Ramayana 0.3)
- **Original**: Contents Invocation. . . . . . . . . . . . . . . . . . . . . . . . . .2 Book I. . . . . . . . . . . . . . . . . . . . . . . . . . . .4 Canto I. Nárad. . . . . . . . . . . . . . . . . . . . . .4 Canto II. Brahmá's Visit . . . . . . . . . . . . . . . . .19 Canto III. The Argument. . . . . . . . . . . . . . . . .26 Canto IV. The Rhapsodists. . . . . . . . . . . . . . . .31 Canto V. Ayodhyá. . . . . . . . . . . . . . . . . . . .35 Canto VI. The King. . . . . . . . . . . . . . . . . . . .38 Canto VII. The Ministers. . . . . . . . . . . . . . . . .43 Canto VIII. Sumantra's Speech. . . . . . . . . . . . . .45 Canto IX. Rishyasring. . . . . . . . . . . . . . . . . .49 Canto X. Rishyasring Invited. . . . . . . . . . . . . . .58 Canto XI. The Sacrifice Decreed. . . . . . . . . . . . .62 Canto XII. The Sacrifice Begun. . . . . . . . . . . . .65 Canto XIII. The Sacrifice Finished. . . . . . . . . . . .69 Canto XIV. Rávan Doomed. . . . . . . . . . . . . . .79 Canto XV. The Nectar. . . . . . . . . . . . . . . . . .84 Canto XVI. The Vánars. . . . . . . . . . . . . . . . .88 Canto XVII. Rishyasring's Return. . . . . . . . . . . .92 Canto XVIII. Rishyasring's Departure. . . . . . . . . .97 Canto XIX. The Birth Of The Princes. . . . . . . . . .100 Canto XX. Visvámitra's Visit. . . . . . . . . . . . . .105 Canto XXI. Visvámitra's Speech. . . . . . . . . . . . .108 Canto XXII. Dasaratha's Speech. . . . . . . . . . . . .111 Canto XXIII. Vasishtha's Speech. . . . . . . . . . . . .114 Canto XXIV. The Spells. . . . . . . . . . . . . . . . .117 Canto XXV. The Hermitage Of Love. . . . . . . . . .120 Canto XXVI. The Forest Of Tádaká. . . . . . . . . . .123 Canto XXVII. The Birth Of Tádaká. . . . . . . . . . .128
- **Translation**: 

---

### Verse 19 (Ramayana 0.4)
- **Original**: iv The Ramayana Canto XXVIII. The Death Of Tádaká. . . . . . . . . .130 Canto XXIX. The Celestial Arms. . . . . . . . . . . .134 Canto XXX. The Mysterious Powers. . . . . . . . . .138 Canto XXXI. The Perfect Hermitage. . . . . . . . . . .140 Canto XXXII. Visvámitra's Sacrifice. . . . . . . . . .144 Canto XXXIII. The Sone. . . . . . . . . . . . . . . . .147 Canto XXXIV. Brahmadatta. . . . . . . . . . . . . . .149 Canto XXXV. Visvámitra's Lineage. . . . . . . . . . .156 Canto XXXVI. The Birth Of Gangá. . . . . . . . . . .159 Canto XXXIX. The Sons Of Sagar. . . . . . . . . . . .162 Canto XL. The Cleaving Of The Earth. . . . . . . . . .165 Canto XLI. Kapil. . . . . . . . . . . . . . . . . . . . .168 Canto XLII. Sagar's Sacrifice. . . . . . . . . . . . . .173 Canto XLIII. Bhagírath. . . . . . . . . . . . . . . . . .176 Canto XLIV. The Descent Of Gangá. . . . . . . . . . .179 Canto XLV. The Quest Of The Amrit. . . . . . . . . .186 Canto XLVI. Diti's Hope. . . . . . . . . . . . . . . . .194 Canto XLVII. Sumati. . . . . . . . . . . . . . . . . . .196 Canto XLVIII. Indra And Ahalyá . . . . . . . . . . . .199 Canto XLIX. Ahalyá Freed. . . . . . . . . . . . . . . .202 Canto L. Janak. . . . . . . . . . . . . . . . . . . . . .204 Canto LI. Visvámitra. . . . . . . . . . . . . . . . . . .207 Canto LII. Vasishtha's Feast. . . . . . . . . . . . . . .210 Canto LIII. Visvámitra's Request. . . . . . . . . . . . .213 Canto LIV. The Battle. . . . . . . . . . . . . . . . . .217 Canto LV. The Hermitage Burnt. . . . . . . . . . . . .220 Canto LVI. Visvámitra's Vow. . . . . . . . . . . . . .224 Canto LVII. Trisanku. . . . . . . . . . . . . . . . . . .227 Canto LVIII. Trisanku Cursed. . . . . . . . . . . . . .230 Canto LIX. The Sons Of Vasishtha. . . . . . . . . . .234 Canto LX. Trisanku's Ascension. . . . . . . . . . . . .236 Canto LXI. Sunahsepha. . . . . . . . . . . . . . . . .241 Canto LXII. Ambarísha's Sacrifice. . . . . . . . . . . .245 Canto LXIII. Menaká. . . . . . . . . . . . . . . . . . .248
- **Translation**: 

---

### Verse 20 (Ramayana 0.5)
- **Original**: v Canto LXIV. Rambhá. . . . . . . . . . . . . . . . . .252 Canto LXV. Visvámitra's Triumph . . . . . . . . . . .255 Canto LXVI. Janak's Speech. . . . . . . . . . . . . . .259 Canto LXVII. The Breaking Of The Bow. . . . . . . .263 Canto LXVIII. The Envoys' Speech. . . . . . . . . . .266 Canto LXIX. Dasaratha's Visit. . . . . . . . . . . . . .268 Canto LXX. The Maidens Sought. . . . . . . . . . . .270 Canto LXXI. Janak's Pedigree. . . . . . . . . . . . . .276 Canto LXXII. The Gift Of Kine. . . . . . . . . . . . .279 Canto LXXIII. The Nuptials. . . . . . . . . . . . . . .281 Canto LXXIV. Ráma With The Axe. . . . . . . . . . .286 Canto LXXV. The Parle. . . . . . . . . . . . . . . . .289 Canto LXXVI. Debarred From Heaven. . . . . . . . .293 Canto LXXVII. Bharat's Departure. . . . . . . . . . .296 BOOK II. . . . . . . . . . . . . . . . . . . . . . . . . . .301 Canto I. The Heir Apparent. . . . . . . . . . . . . . .301 Canto II. The People's Speech. . . . . . . . . . . . . .305 Canto III. Dasaratha's Precepts. . . . . . . . . . . . . .310 Canto IV. Ráma Summoned. . . . . . . . . . . . . . .316 Canto V. Ráma's Fast. . . . . . . . . . . . . . . . . . .322 Canto VI. The City Decorated. . . . . . . . . . . . . .325 Canto VII. Manthará's Lament. . . . . . . . . . . . . .328 Canto VIII. Manthará's Speech. . . . . . . . . . . . . .332 Canto IX. The Plot. . . . . . . . . . . . . . . . . . . .337 Canto X. Dasaratha's Speech. . . . . . . . . . . . . . .344 Canto XI. The Queen's Demand. . . . . . . . . . . . .349 Canto XII. Dasaratha's Lament. . . . . . . . . . . . . .352 Canto XIII. Dasaratha's Distress. . . . . . . . . . . . .365 Canto XIV. Ráma Summoned. . . . . . . . . . . . . .367 Canto XV. The Preparations. . . . . . . . . . . . . . .375 Canto XVI. Ráma Summoned. . . . . . . . . . . . . .381 Canto XVII. Ráma's Approach. . . . . . . . . . . . . .387 Canto XVIII. The Sentence. . . . . . . . . . . . . . . .389 Canto XIX. Ráma's Promise. . . . . . . . . . . . . . .394
- **Translation**: 

---

