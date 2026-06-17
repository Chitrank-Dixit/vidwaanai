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

### Verse 1 (Vaivtpuran 543.13514)
- **Original**: तटपर जाकर शंकरके ध्यान और पूजनके पश्चात्‌ मूलप्रकृति ईश्वरी जगदम्बाकों जगत्पिता महादेवजीके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13515)
- **Original**: उनके चरणारविन्दोंका चिन्तन करती हुई सुन्दरी हाथमें देकर कृतकृत्य हो जाओ। सतीने शरीरको त्याग दिया और गन्धमादन पर्वतकी गिरिराज ! कल्पान्तरकी बात है; वह मूलप्रकृति
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13516)
- **Original**: गुफामें विद्यमान उस दिव्य विग्रहमें प्रवेश किया, ईश्वरी भगवान्‌ श्रीकृष्णकी आज्ञासे दक्षकन्या सतीके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13517)
- **Original**: जिसके द्वारा उसने पूर्वकालमें दैत्योंके समस्त रूपमें आविर्भूत हुई। दक्षने उस देवोको विधि-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13518)
- **Original**: कुलका संहार किया था। वह घटना देख सब देवता विधानके साथ शूलपाणि शिवके हाथमें दे दिया।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13519)
- **Original**: अत्यन्त विस्मित हो हाहाकार कर उठे। शंकरके तदनन्तर मेरे पिताके यज्ञ्में, जहाँ समस्त देवताओंकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13520)
- **Original**: सैनिक दक्ष-यज्ञका विनाश तथा सबका पराभव सभा जुड़ी हुई थी, दक्षकां उन शूलपाणि महादेवजीके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13521)
- **Original**: करके शोकसे व्याकुल हो लौट गये और शीघ्र ही साथ सहसा महान्‌ कलह हो गया। उस कलहसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13522)
- **Original**: सारा वृत्तान्त अपने स्वामीसे कह सुनाया। वह रुष् हो त्रिनेत्रधारी शिव ब्रह्माजीको नमस्कार करके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13523)
- **Original**: समाचार सुनकर समस्त रुद्रगणोंसे घिरे हुए संहारकारी चले गये। दक्षके मनमें भी रोष था; अत: वे भी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13524)
- **Original**: महेश्वर गड्भाजीक उस तटपर गये, जहाँ देवी अपने गणोंके साथ उसी क्षण अपने घरको चल
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13525)
- **Original**: सतीका शरीर पड़ा था। दिये। घंर जाकर दक्षने रोषपूर्वक ही यज्ञको सामग्री
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13526)
- **Original**: (अध्याय 42) ध >> 56490000
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13527)
- **Original**: * श्रीकृष्णजन्मखण्ड « 587 अऋऋ#### ## # कक 54444 54%%$%4 44 &#% # 5 55% 546 ## ## 4 % $ ऋऋ ऋ#ऋ### 6 # # # 4 4 हक ऋ#### 6 # ## शिवका सतीके शवको लेकर शोकबश समस्त लोकोंमें भ्रमण, भगवान्‌ विष्णुका उन्हें समझाना और प्रकृतिकी स्तुतिके लिये कहना, शिवद्वारा की हुई स्तुतिसे संतुष्ट हुईं प्रकृतिरूपिणी सतीका शिवको दर्शन एवं सान्त्वना देना श्रीनारायण कहते हैं--नारद! तदनन्तर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13528)
- **Original**: अध्यात्मज्ञानका सार, दुःख-शोकका नाश करनेवाली महादेवजीने गज्जाजीके तटपर सोयी हुई दुर्गास्वरूपा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13529)
- **Original**: तथा सम्पूर्ण अध्यात्मज्ञानका विद्यमान बीज है। सतीकी मनोहर मूर्ति देखी, जिसके मुखारविन्दकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13530)
- **Original**: यद्यपि तुम स्वयं ज्ञानकी निधि, विधि, सर्वज्ञ कान्ति अभी मलिन नहीं हुई थी। वह शरीरपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13531)
- **Original**: तथा स्स्‍ष्टाओंके भी स्रष्टा हो, तथापि मैं तुम्हें थेत वस्त्र धारण किये और हाथमें अक्षमाला
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13532)
- **Original**: ज्ञाकका उपदेश दे रहा हूँ। प्राण-संकटके समय लिये टिव्य तेजसे प्रकाशित हो रही थी। उसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13533)
- **Original**: विद्वान्‌ पुरुष विद्वानकों भी समझा सकता है। अब्जोंसे तपाये हुए सुवर्णकी-सी कमनीय कान्ति
- **Translation**: 

---

