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

### Verse 1 (Vaivtpuran 543.12454)
- **Original**: निहारती हुई बैठ गयीं। उन सबके मुखपर प्राणस्वरूपा हो। प्यारी गोपियो! तुमलोगोंका यह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12455)
- **Original**: प्रसन्नता छा रही थी; मन्द मुस्कानकी प्रभा फैल व्रत लोकरक्षाके लिये है, स्वार्थसिद्धिके लिये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12456)
- **Original**: रही थी। वे प्रेमपूर्वक बाँकी चितवनसे देखती नहीं; क्योंकि तुमलोग गोलोकसे मेरे साथ आयी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12457)
- **Original**: हुई अपने नेत्र-चकोरोंद्वारा श्रीहरिके मुखचन्द्रकी हो और फिर मेरे साथ ही तुम्हें वहाँ चलना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12458)
- **Original**: सुधाका पान कर रही थीं। तत्पश्चात्‌ वे बारंबार है। (तुम मेरी नित्यसिद्धा प्रेयसी हो। तुमने साधन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12459)
- **Original**: जय बोलकर शीघ्र ही अपने-अपने घर गयीं करके मुझे पाया है, ऐसी बात नहों है।) अब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12460)
- **Original**: और श्रीकृष्ण भी ग्वाल-बालोंके साथ प्रसन्नतापूर्वक शीघ्र अपने घर जाओ। मैं जन्म-जन्ममें तुम्हारा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12461)
- **Original**: अपने घरकों लौटे। इस प्रकार मैंने श्रीहरिका ही हूँ। तुम मेंरे लिये प्राणोंसे भी बढ़कर हो;
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12462)
- **Original**: यह सारा मज्जलमय चरित्र कह सुनाया, गोपीचीर- इसमें संशय नहीं है। हरणकी यह लीला सब लोगोंके लिये सुखदायिनी ऐसा कहकर श्रीहरि वहीं यमुनाजीके किनारे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12463)
- **Original**: है। (अध्याय 27) ध>्िदा900> श्रीकृष्णके रास-बिलासका वर्णन नारदजीने पूछा-- भगवन्‌ ! तीन व्यतीत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12464)
- **Original**: बहनेवाली शीतल, मन्द एवं सुगन्धित मलयवायुसे होनेपर उन गोपाड्नाओंका श्रीहरिके साथ किस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12465)
- **Original**: सारा वनप्रान्‍्त सुवासित हो रहा था। भ्रमरोंके प्रकार मिलन हुआ ? वृन्दावन कैसा है ? मधुर गुझारवसे उसकी मनोहरता बढ़ गयी थी। क्या स्वरूप है? श्रीकृष्ण तो एक थे और गोपियाँ वृक्षोंमें नये-नये पल्लव निकल आये थे और बहुत। ऐसी दशामें किस तरह वह क्रीड़ा सम्भव
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12466)
- **Original**: कोकिलकी कुहू-कुहू-ध्वनिसे वह वन मुखरित हुई? मेरे मनमें इस नयी-नयो लीलाको सुननेके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12467)
- **Original**: हो रहा था। नौ लाख रासगृहोंसे संयुक्त वह लिये बड़ी उत्सुकता हो रही है। महाभाग! आपके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12468)
- **Original**: वृन्दावन बड़ा ही मनोहर जान पड़ता था। चन्दन, नाम और यशका श्रवण एवं कीर्तन बड़ा पवित्र
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12469)
- **Original**: अगुरु, कस्तूरी और कुंकुमकी सुगन्‍्ध सब ओर है। कृपया आप उस रासक्रौड़ाका वर्णन कीजिये।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12470)
- **Original**: फैल रही थी। कर्पूरयुक्त ताम्बूल तथा भोग- अहो ! श्रीहरिकी रासयात्रा, पुराणोंक सारकी भी [द्रव्य सजाकर रखे गये थे। कस्तूरी और सारभूता कथा है। इस भूतलपर उनके द्वारा की
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12471)
- **Original**: चन्दनयुक्त चम्पाके फूलोंसे रचित नाना प्रकारकी गयी सारी लोलाएँ ही सुननेमें अत्यन्त मनोहर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12472)
- **Original**: शब्याएँ उस स्थानकी शोभा बढ़ा रही थीं। रत्रमय जान पड़ती हैं। प्रदीपोंका प्रकाश सब ओर फैला था। धूपकी सूतजी कहते हैं--शौनक! नारदजीकी यह
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12473)
- **Original**: सुगन्धसे वह वनप्रान्त महमह महक रहा था। बात सुनकर साक्षात्‌ नारायण ऋषि हँसे और
- **Translation**: 

---

