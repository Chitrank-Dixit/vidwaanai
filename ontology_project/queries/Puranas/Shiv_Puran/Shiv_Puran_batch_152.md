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

### Verse 1 (Shiv Puran 0.3021)
- **Original**: त्रियूल, बजञ्र, परशु, थाण, खड्ग,
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.3022)
- **Original**: क्र छ<8प5्‌ है क्त#7#2-4####ै+#ै #%# # #* # # # #है/ 4 # हैं 4++40+#+# “कक कक जैकेट 00% 00447 कक ॑4 0 घ 0 कै घयय पादा, अछ्ुश और श्रेष्ठ आयुध पिनाक--ये महादेव तथा महादेलवीके दिव्य आयुध शिव और शिवाकी आज्ञाका नित्य सल्कार करते हुए सदा मेरी रक्षा करें
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.3023)
- **Original**: 940-149
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.3024)
- **Original**: वृषरूपपरों' देकः सौरभेयो महायलः
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.3025)
- **Original**: वड़वाक््यानलस्पद्धी पमगोमातृधिर्ततः
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.3026)
- **Original**: खाहनत्वमनुप्राप्नस्तपसा फरमेशायोः । तयोराजा पुरस्कृत्प स से कामे प्रयच्छतु
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.3027)
- **Original**: युषभरूपधारी देव, जो सुरभिके महाबली पुत्र हैं, बड़बानलसे भी होड़ लगाते हैं, पाँच गोमाताओंसे घिरे रहते हैं और अपनी तपस्याके प्रभावसे परमेश्वर झित तथा परमेश्वरी शिवाके वाहन हुए हैं, उन दोनोंकी आज्ञा शिरोथार्य करके पेरी इच्छा पूर्ण करें
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.3028)
- **Original**: 142-143
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.3029)
- **Original**: नन्‍्दा सुनन्दा सुरक्षि सुशील्त्र सुपनास्तथा
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.3030)
- **Original**: चह्क गोमातरस्त्वेता: झिवलोके व्यवस्थिता:
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.3031)
- **Original**: जिवभक्तिपर नित्ये.. विधार्यचनपरायणा: । दिवय्तेः पासनादेव दिशन्तु मम चाउसतस्‌
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.3032)
- **Original**: 14णत। नन्‍्दा, सुनन्‍्दा, सुरभि, सुझीक्ल और सुमना--ये पाँच गोमाताएँ सदा शिवल्ठोकमें निवास करती हैं। ये सब-की-सब्र नित्य झिबा्ननमें लूगी रहती और झिवभक्ति- परायणा हैं, अतः हि तथा शिवराके आदेशसे ही मेरी इच्छाकी पूर्ति करें
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.3033)
- **Original**: 144-945
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.3034)
- **Original**: । क्षेत्रपलो महातेज़ा नीलजीमूतसंनिभ:
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.3035)
- **Original**: दष्टाकशाललदन:. स्फुरक्ताधग्रेज्ज्वकः
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.3036)
- **Original**: रहर्ष्यमूर्दज: ओमान्‌ धुकुटीकुटिलेखण: । सक्तयृत्तत्रिनवन: आविपन्नगभूषण:
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.3037)
- **Original**: नम्नखिशूलपान्नासिकपास्नेच्चतपाणिक:
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.3038)
- **Original**: चैरवों पैर: सिद्धेयोगिनॉमिश सैयृतः
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.3039)
- **Original**: औजे क्षेत्रसमासीनः स्थितों यो रक्षक: सताम्‌ । शिकप्रणामपरम:... शिवसद्धावधायितः
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.3040)
- **Original**: शिजाश्रितान्‌ विद्ेषेण रक्षन्‌ पुत्रानिवौरसान्‌। सत्कृत्व शिवयोराज्ञों स मे दिशत्‌ मड्रलम्‌
- **Translation**: 

---

