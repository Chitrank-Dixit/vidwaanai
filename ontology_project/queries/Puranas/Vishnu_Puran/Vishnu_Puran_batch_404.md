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

### Verse 1 (Vishnu Puran 0.8061)
- **Original**: 486-47
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8062)
- **Original**: तदनन्तर यह अक्षय, वीर्य, ज्ञौर्य, सम्पत्ति और पराक्रम आदि गुणोंसे सम्मन्न तथा समस्त त्रिभुवनके स्वामी इन्द्रके भी प्रभावको दबानेवाला दशानन हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8063)
- **Original**: स्वयं भगवानके हाथसे ही मारे जानेके पुण्यसे प्राप्त हुए नाना भोगोंको बह बहुत समयग्रतक भोगते हुए अन्तमें राघवरूपथारी भगवानके ही ड्ाय सारा गया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8064)
- **Original**: उसके पीछे यह चेदिराज दमघोषका पुत्र शिशुपाल हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8065)
- **Original**: शिश्ुपाल होनेपर भो वह भू-भार-हरणफे लिये अचत्ोर्ण हुए भगवरदंश- स्वरूप भगवान्‌ पुण्डरीकाक्षमें अत्यत्त द्वेषबुद्धि करने लूगा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8066)
- **Original**: अन्तां भगवानके हाथसे ही मारे जानेपर उन परमात्मामें ही मन लगे रहनेके कारण सायुज्य-मोक्ष भ्राप्त किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8067)
- **Original**: भगवान्‌ यदि प्रसन्न होते हैं तब जिस प्रकार य्थेच्छ फल देते हैं, ठसी प्रकार अप्रसन्न होकर सारतेपर भी वे अनुपम दिव्यल्थेककी प्राप्ति कराते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8068)
- **Original**: 20-_-- जी “लत इति श्रीबिष्णुपुराणे चतुर्थेष्ञे चतुर्दशोउध्याय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8069)
- **Original**: । बन जे “++++ पत्रहवाँ अध्याय शिशुपालके पूर्व-जन्पान्तरोंका तथा वसुदेवजीकी सन्‍्ततिका वर्णन श्रीमैत्रेय उवाच हिरण्यकशिपुल्बे चर रावणत्वे च्र विष्णुना । अबाप निहतो भोगानप्राप्यानमरैरपि
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8070)
- **Original**: 19 न लय॑ तत्न तेनेव निहतः स कर्थ पुनः । सम्प्राप्त: शिशुपालत्वे सायुज्यं शाश्वते हरो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8071)
- **Original**: 2 श्रोतुं सर्वधर्मभूतां बर। कौतूहलपरेणैतत्यूष्टो- मे. वक्तुमहसि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8072)
- **Original**: 3 आपराशर उबनाच दैत्येश्वरस्य वधायाखिललोकोत्पत्ति- स्थितिविनाशकारिणा पूर्व तनुग्रहणं कुर्वता नृसिंहरूपपातिष्कृतम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8073)
- **Original**: तत्र च्॒ हिरण्य- मनस्थभूत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8074)
- **Original**: श्रीमैत्रेयजी . बोले--भगवन्‌ ! . पूर्वजन्मोमें हिरण्यकशिपु और ग्वण होनेपर इस झिजुपालने भगवान्‌ निष्णुके द्वारा मारे जानेसे देव-दुर्लम भोगोंको तो प्राप्त किया, किन्तु यह उनमें ल्तैन नहों हुआ; फिर इस जच्ममें ही डनके द्वारा मारे जानेपर इसने सनातन पुरुष श्रीहरिसें सायुज्य मोक्ष कैसे प्राप्त किया ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8075)
- **Original**: है समस्त धर्मात्माओमें श्रेष्ठ मुनिवर ! यह बात सुननेकी मुझे बड़ी ही इच्छा है। गैंने अत्यन्त कुतृहलवश होकर आपसे यह प्रश्न किया है, कृपया इसका निरूपण कीजिये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8076)
- **Original**: श्रीपराशरजी बोले--प्रथा जन्मों दैत्पतान हिरण्यकशिपुका बध करनेके ठिल्ये सम्पूर्ण लोकॉको उत्पत्ति, स्थिति और नादा करनेवाले भगवानने शरीर परहण करते समय नृसिंहरूप प्रकट किया था।। 4
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8077)
- **Original**: उस समय चित्तमें यह भाव नहीं हुआ था कि ये हिरण्यकशिपुके निरतिशयपुण्यसमुद्धृतमेतत्सत्तजातमिति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8078)
- **Original**: विष्णुभगवान्‌ हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8079)
- **Original**: केवल इतना हो विचार हुआ कि किल पु 10--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8080)
- **Original**: स्थ्ड श्रीविष्णुपुराण [ अ0 17 रज उद्देकप्रेरितिकाग्रमतिस्तद्धावनायोगात्ततो5वाप्त-
- **Translation**: 

---

