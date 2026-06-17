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

### Verse 1 (Vishnu Puran 0.2641)
- **Original**: 29 ते पिता मूर्थ््युपाप्राय परिष्ृज्य च पीडितम्‌ । जीवसीत्याह वत्सेति बराष्पादनयनों द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2642)
- **Original**: 30 प्रीतिमांश्षाउ3भवत्तस्पिन्ननुतापी महासुरः । गुरुपित्रोश्चकारैव शुश्रूषां सोडपि धर्मवित्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2643)
- **Original**: 31 पितर्युपरति नीते . नरसिंहस्वरूपिणा । विष्णुना सो5पि दैत्यानां मैत्रेयाभूत्पतिस्ततः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2644)
- **Original**: 32 ततो राज्ययुति प्राप्य कर्मशुद्धिकरीं द्विज । पुत्रपोत्रांध सुबहूनवाप्पैश्वयमेव च
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2645)
- **Original**: 33 क्षीणाधिकार: स यदा पुण्यपापविवर्जितः । तदा स भगवद्धबानात्पर निर्वाणमाप्तवान्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2646)
- **Original**: 34 एवं प्रभावो दैत्योउसौ म्रैश्नेयासीन्‍्पहासतिः । प्रह्मदों भगवद्धक्तो य॑ त्व॑ मामनुपृष्छसि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2647)
- **Original**: 35 यस्त्वेतशवरित तस्य प्रह्लादस्प महात्मन: । शरृणोति तस्य पापानि सद्दो गच्छन्ति सद्बुयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2648)
- **Original**: 36 अहोरात्रकृतं पाप॑ प्रह्मादवरित॑ नरः । श्रृण्वन्‌ पठंश्न पैत्नेय व्यपोहति न संशय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2649)
- **Original**: 37 पौर्णमास्याममावास्थामष्टम्यामथ वा पठन्‌। द्वादश्यां वा तदाप्नोति गोप्रदानफर्ल द्विज
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2650)
- **Original**: 38 प्रहांदे सकलापत्सु यथा रक्षितवान्हरिः । तथा रक्षति यस्तस्प श्रूणोति चरित सदा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2651)
- **Original**: 39 अ्रह्वादजी खोले--हे भगवन्‌ ! मैं तो आपके इस बरसे ही कृतकृत्य हो गया कि आपकी कृपासे आपमें मेरी निरन्तर अविचल भक्ति रहेगी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2652)
- **Original**: है प्रभो ! सम्पूर्ण जगतके कारणरूप आपमें जिसकी निश्चल भक्ति है, मुक्ति भो उसकी मुट्टीमें रहतो है, फिर धर्म, अर्थ, कामसे तो उसे लेना ही क्या है ?
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2653)
- **Original**: श्रीभगवान्‌ बोले--हे प्रह्माद ! मेरी भक्तिसे युक्त तेश चित्त जैसा निश्चल है उसके कारण तू मेरी कृपासे परम निर्वाणपद प्राप्त करेगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2654)
- **Original**: श्रीपराशसरजी बोले--हे मैत्रेय !: ऐसा कह भगवान्‌ उनके देखते-देखते अन्तर्धान हो गये; और उन्होंने भी फिर आकर अपने पिताके चरणोंकी वन्दना की
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2655)
- **Original**: हे द्विज ! तब पिता हिरण्यकशिपुने, जिसे नाना प्रकारसे पीडित किया था उस पुतन्नका सिर सुँपकर, आँखोंमें आँसू भरकर कहा--'“बेटा, जीता तो है !'
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2656)
- **Original**: वह महान्‌ असुर अपने कियेपर पछताकर फिर अह्ाादसे प्रेम करते लगा और इसी प्रकार धर्मज्ञ प्रह्मदजी भी अपने गुरु और माता-पिताकी सेवा-शुश्रूषा करने रको
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2657)
- **Original**: है मैत्रेय ! तदनस्तर नृसिहरूपधारी भगवान्‌ विष्णुद्वारा पिताके मारे जानेपर ले दैल्योंके राजा हुए
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2658)
- **Original**: हे द्विज ! फिर प्रारब्धक्षयकारिणी राज्यलक्ष्मी, बहुत से पुत्र-पौषादि तथा परम ऐश्वर्य पाकर, कर्माघिकारके क्षीण होनेपर पुण्य-पापसे रहित हो भगवान्‌का ध्यान करते हुए उन्होंने परम निर्वाणपद प्राप्त किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2659)
- **Original**: 33-वे4
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2660)
- **Original**: हे मैत्रेय
- **Translation**: 

---

