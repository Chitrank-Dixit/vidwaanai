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

### Verse 1 (Vishnu Puran 0.4781)
- **Original**: 5 वीर्य तेजो बल चालपं मनुष्याणामवेक्ष्य च । हिताय सर्वभूतानां वेदभेदान्करोति सः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4782)
- **Original**: 6 ययासौ कुरुते तन्‍्वा वेदमेक॑ पृथक्‌ प्रभु: वेदव्यासाभिथधाना तु सा चल मूर्तिमधुद्विष:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4783)
- **Original**: 7 श्रीपैज्रेयजी जोले-- हे भगवन्‌ ! आपके कथनसे मैं यह जान गया कि किस प्रकार यह सम्पूर्ण जगत्‌ विष्णुरूप है, विष्णुमें हो स्थित है, निष्णुसे ही उत्पन्न हुआ है तथा विष्णुसे अतिरिक्त और कुछ भी नहीं है ?
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4784)
- **Original**: अब मैं यह सुनना चाहत्त हूँ कि भगवानने लेदव्यासरूपसे युग-युण्ें किस प्रकार वेदोंका बरिभाग क्रिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4785)
- **Original**: हे महामुने ! हे भगवन्‌ । जिस-जिस युगमें जो-जो बेदव्यास हुए उनका तथा बेदॉंके सम्पूर्ण झाखा-भेदोंका आप मुझसे वर्णन कोजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4786)
- **Original**: श्रीपराहरजी खोले--हे #त्रेय ! बेदरूप वृक्षके सहस्त्रों शाखा-भेट हैं, उनका चिस्तारसे वर्णन करतमेमें तो कोई भी समर्थ नहीं है, अत: संक्षेपसे सुनो-+
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4787)
- **Original**: है महामुने ! प्रत्येक द्वापरयुगमें भगवान्‌ विष्णु ज्यासरूपस अबतीर्ण होते है और संसारके कल्याणके ल्त्ये एक;-बेदके अनेक भेद कर देते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4788)
- **Original**: मनुष्योंके बल, नीर्य और तेजको अल्प जानकर वे समस्त प्राणियोंके हितके ट्थ्यि बेदोंका विभाग करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4789)
- **Original**: जिस दारीरके द्वारा जे प्रम॒ एक चेदके अनेक विभाग करते हैं भगवान्‌ मधुसूदगर्की उस मूर्तिका नाम वेटव्यास है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4790)
- **Original**: यस्मिन्‍्म्न्वत्तरे व्यासा ये ये स्पुस्तान्निबो ध पे । तृतीय अंक्ष 1791 हे मुने ! जिस-जिस मन्वन्तरमें जो-जो व्यास होते हैं यंथा च भेटइशास्तानां व्यासेन क्रियते मुने
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4791)
- **Original**: और वे जिस-जिस प्रकार द्ास्षाओका विभाग करते अष्टराविंञ्तिकृत्वो वे बेदो व्यस्तो महर्षिभि: । खैवस्वतेउन्तरे ततस्मिन्हापरेषु पुनः पुनः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4792)
- **Original**: 9 वेदव्यासा व्यतीता ये ह्ाष्टाविंशति सत्तम । चतुर्धा यैः कृतो वेदों ह्वापरेषु पुनः पुनः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4793)
- **Original**: 10 ड्ापरे प्रथमे व्यस्तस्स्वयं वेद: स्वयप्युवा । ह्वितीये द्वापरे चैब वेदव्यासः प्रजापति:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4794)
- **Original**: 11 तृतीये चोझना व्यासशअ्रतुर्थे च बृहस्पतिः । सविता पञ्ममे व्यास: षष्टे मृत्युस्स्मृत: प्रभु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4795)
- **Original**: 92 सप्तमे च तथैवेन्द्रो वसिष्ठश्नाप्टमे स्मृतः । सारस्वतश्च नवमे श्रिधामा दहमे स्मृत:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4796)
- **Original**: 13 एकादडो तु त्रिज्चिखो भरद्वाजस्तत: पर: । अ्रयोदशे चान्तरिक्षों वर्णी चापि चतुर्दशे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4797)
- **Original**: 14 अ्रय्यारुगः पश्खदशे षोडशे तु धनज्ञय: । ऋतुकझ्षयः सप्तदशे तदूध्व॑ च जयस्स्मृत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4798)
- **Original**: 15 ततो व्यासो भरद्वाजो भरद्वाजाच्च गौतमः । गौतमादुत्तरो व्यासो हर्यात्मा योडभिधीयते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4799)
- **Original**: 16 अथ हर्यात्मनो5न्ते च स्मृतो बाजश्रवा मुनि: । सोमशुष्मायणस्तस्मात्तणबिन्दुरिति स्मृत:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4800)
- **Original**: 17 ऋक्षो$भूद्धार्गवस्तस्माद्माल्मीकियों 5भिधीयते । तस्मादस्मत्यिता शक्तिव्यासस्तस्मादह घुने
- **Translation**: 

---

