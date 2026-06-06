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

### Verse 1 (Vishnu Puran 0.6161)
- **Original**: 52 श्रूयते च पुरा ख्यातो राजा शातधनुर्भुवि । पत्नी च् जैव्या तस्याभूदतिधर्मपरायणा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6162)
- **Original**: 53 पतिब्रता महाभागा सत्वशौचदयान्विता । सर्वल्छक्षणसम्पन्ना विनयेन नयेन च
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6163)
- **Original**: (4 स तु राजा तया साद् देवदेव॑ जनार्दनम्‌। आराधयामास विभुं परमेण समाधिना
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6164)
- **Original**: 55 होमैर्जपैस्तथा दानैरुपवासैश भक्तित: । पूजाधिश्चानुदिवर्स व्तन्‍्मना नान्यमानस:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6165)
- **Original**: 56 एकदा तु सम॑ स््रातों तौ तु भार्यापती जले । भागीरथ्यास्समुत्तीर्णो कार्त्तिक्यां समुपोषितो । पाषण्डिनमपश्येतामायान्तं सम्मुख द्विज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6166)
- **Original**: 57 चापाचार्यस्य तस्यासो सखा राज़ो महात्मन: । अतस्तद्रौरवात्तेन सखाभावमथाकरोत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6167)
- **Original**: 58 नतु सा वाम्यता देवी तस्व पत्नी पतिग्रता । उपोषितास्मीति रविं तस्मिन्दृष्टे दरदर्श च
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6168)
- **Original**: 59 समागम्य यथान्याय॑ दम्पती तौ यथाविधि । बिष्णो: पूजादिक सर्ब॑ कृतवन्तौ द्विजोत्तम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6169)
- **Original**: 60 कालेन गच्छता राजा ममारासौ सपल्नजित्‌ । अन्वारुरोह त॑ देवी चितास्थे भूपतिं पतिम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6170)
- **Original**: 61 [ अ*0 18 करता है वह शीघ्र ही उसीके समान हो जाता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6171)
- **Original**: ओ मनुष्य देवता, पितर, भूतगण और अतिथियॉका पूजन किये थिना स्वयं भोजन करता है चह्द पापमय भोजन करता है; उसकी शुभगति नहीं हो सकती
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6172)
- **Original**: जो ब्राह्मणादि वर्ण स्वधर्मको छोड़कर परचर्मामें प्रवृत्त होते हैं अथवा हीनवृत्तिका अवलम्बन करते हैं ले 'नम्र' कहत्वते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6173)
- **Original**: हे मैत्रेय ! जिस स्थानमें चारों वर्णोका अत्यन्त मिश्रण हो उसमें रहनेसे पुरुषकी साथुवत्तियोंका क्षय हो जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6174)
- **Original**: जो पुरुष ऋषि, देव, पितृ, भूत, और अतिथिगणका पूजन किये त्रिना भोजन करता है उससे समप्पाषण करनेसे भी स्प्रेग नस्कमें पड़ते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6175)
- **Original**: अतः बेदत्रयीके त्यागसे दूषित इन नम्नोंके साथ प्राजपुरुष सर्वदा सम्भाषण और स्पर्श आदिका भी त्याग कर दे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6176)
- **Original**: यदि इनको दृष्टि पड़ जाय तो श्रद्धानान्‌ पुरुषोंका यत्रपूर्वक किया हुआ श्राद्ध देवता अथवा पितृपितामहगणकी तृप्ति नहीं करता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6177)
- **Original**: सुना जाता है, पूर्वकालमें पृथिवीत्ततपर शतधन्‌ नामसे विख्यात एक राजा था। उसकी पत्नी दौव्या अत्यन्त धर्मपरायणा थी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6178)
- **Original**: वह महाभागा पतित्रता, सत्य, शौच और दयासे युक्त तथा विनव और नीति आदि सम्पूर्ण सुलक्षणोंसे सम्पन्न थी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6179)
- **Original**: उस महारानीके साथ राजा झतथनुने परुम-समाधिद्वारा सर्वव्यापक, टेवदेव श्रीजनार्दनकी आराधना की
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6180)
- **Original**: वे प्रतिदिन ठनन्‍्मय होकर अनन्यभावसे होम, जप, दान, उपवास और पृजन आदिद्वारा भगवान्‌की भक्तिपूर्वक आराधना करने लगें
- **Translation**: 

---

