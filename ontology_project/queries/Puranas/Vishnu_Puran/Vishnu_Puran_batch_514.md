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

### Verse 1 (Vishnu Puran 0.10261)
- **Original**: 15 ततस्तलघप्रहारेण कृष्णस्तस्थ दुरात्मन: । पातयामास रोषेण रजकस्य शिरों भुवि
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10262)
- **Original**: 16 हत्वादाय च॒ बस्न्‍्राणि पीतनीलाम्बरों ततः । कृष्णरामौ मुद्रा युक्तो मालाकारगृह गतो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10263)
- **Original**: 97 विकासिनेत्रयुगलो मालाकारो5तिविस्मित: । एतौ कस्य सुतौ यातो मैत्रेयाचिन्तयत्तदा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10264)
- **Original**: 18 पीतनीलाम्बरधरो तौ दृष्ट्ठातिमनोहरो । स तर्कयामास तदा भुवं देवाबुपागतो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10265)
- **Original**: 19 विकासिमुखपश्माध्यां ताभ्यां पुष्पाणि याचितः । भ्रुव॑ विष्टम्य हस्ताभ्यां पस्पर्श शिरसा महीम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10266)
- **Original**: 20 प्रसादपरमा नाथो मम गेहसमुपागतो । धन्यो5हमर्चयिष्यामीत्याह तौ पाल्यजीवन:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10267)
- **Original**: 29 ततः प्रहषष्टटदनस्तयो: पुष्पाणि कामतः। चारूण्येतान्यथैतानि प्रददौ स प्रलोभयन्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10268)
- **Original**: 22 पुनः पुनः प्रणम्योभौ मालाकारों नरोत्तमो । ददौ पुष्पाणि चारूणि गन्धवन्यमलानि च
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10269)
- **Original**: 23 म्रालाकाराय कृष्णो5पि प्रसन्न: प्रददों वरान्‌ । श्रीस्त्वां मत्संश्रया भद्र न कदाचिक््यजिष्यति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10270)
- **Original**: 24 फश्चम अंश 3619 गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10271)
- **Original**: मधथुरापुरीको देखकर अक्रूरने राम और कृष्णसे कहा--''हे वीरबरों ! अब मैं अकेला ही रथसे जाऊँगा, आप दोनों पैदल चले आवें
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10272)
- **Original**: मथुग़में पहुँचकर आप बसुदेवजीके घर न जायें क्योंकि आपके कारण ही उन वृद्ध वसुदेवजीका केस सर्वदा निरादर करता रहता है”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10273)
- **Original**: ओऔपराशरजी _ खोलछे--ऐसा कह--अक्रूरजी मथुरापुरीमें चले गये। उनके पीछे राम और कृष्ण भी नगस्में प्रयेशकर राजसार्गपर आये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10274)
- **Original**: वहाँके नर नारियोंसे आनन्दपूर्वक देखे जाते हुए वे दोनों वीर मतवाले तरुण हाथियोंकि समान ल्त्रैलापूर्वक जा रहे थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10275)
- **Original**: मार्गमें उन्होंने एक खख्त्र रैगनेबास्टे रजकको घूमते देख उससे स्कू-विरज्जे सुद्दर वस्त्र माँगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10276)
- **Original**: वह रजक कंसका था और राजाके मुँहलूगा होनेसे बड़ा घमण्डी हो गया था, अतः राम और कृष्णके बस्तर माँगनेपर डसने विस्मित होकर उनसे ये जोरॉँके साथ अनेक दुर्वाक्य करे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10277)
- **Original**: तब श्रौकृष्णचद्धने क्रुद होकर अपने करतलके प्रहस्से उस्र दुष्ट रजकका सिर पृथिवोपर गिरा दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10278)
- **Original**: इस प्रकार उसे गारकर राम और कृष्णने डसके वस्त्र छीन लिये तथा क्रमशः नी और पोत बस्तर घारणकर वे प्रसश्नचित्तसे मालीके घर गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10279)
- **Original**: हे मैत्रेय ! उन्हें देखते ही उस मात्जैके नेत्र आनन्‍दसे खिल गये और बह आश्चर्यचकित होकर सोचने लगा कि “ये किसके पुत्र हैं और कहाँसे आये हैं ?'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10280)
- **Original**: पीले और नॉले वस्त्र धारण किये उन अति मनोहर बालकोंको देखकर उसने समझा मानो दो देवगण ही पृथिजीतलूपर पथारे हैं
- **Translation**: 

---

