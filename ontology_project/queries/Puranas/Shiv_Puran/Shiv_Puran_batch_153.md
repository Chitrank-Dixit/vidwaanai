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

### Verse 1 (Shiv Puran 0.3041)
- **Original**: क्षेत्रपाक महान्‌ तेजस्वी हैं; उनकी अड्डकान्ति नील मेघके-समान है और मुख दाढ़ोंक कारण खिकरालू जान पड़ता है। उनके लाल-लाल ओठ फड़कते रहते हैं, जिससे उनकी शोभा अढ़ जाती है, उनके सिसके बाल भी ल्वाल्ल और ऊपरको उठे हुए हैं। वे तेजस्वी हैं, उनकी भौहिं तथा आँखें भी टेढ़ी ही हैं। वे लाल और गोलाकार तीन नेत्र धारण करते हैं। ऋनद्रमा और सर्प उनके आशभूषण हैं। वे सदा नंगे ही रहते हैं तथा उनके हाथोंमें त्रिशूल, पाक्ष, खड़ग और कपाल उठे रहते हैं। ले भैरव हैं और भैरवों, सिद्धों तथा योगिनियोंसे छिरे रहते हैं। अत्येक क्षेत्रमें उनको स्थिति है। वे यहाँ सत्पुरुषोंके रक्षक होकर रहते हैं। उनका मस्तक सदा शिवके चअरणॉपें झुका रहता है, वे सदा शिवके सद्धावसे भावित हैं तथा शिवके दारणागत भक्तोंकी औरस पुञ्नोंकी 'भाँति विशेष रक्षा करते हैं। ऐसे प्रभावशाली क्षेत्रपाक्त शिव और शिवॉकी आज्ञाका सत्कार करते हुए सुझे मड्जल प्रदान करें
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.3042)
- **Original**: 146--150
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.3043)
- **Original**: तालजद्भादयस्तस्य अथाज़वरणेजर्चेता: । रत्कृत्य शिवयोदज्ञों चत्वारः समल्न्तु माम्‌ #₹51
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.3044)
- **Original**: तालजड् आदि शिवके. अथम आकबरणमें पूजित हुए हैं, वे चारों देखता शिवकी आज्ाका आदर करके मेरी रक्षा करें
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.3045)
- **Original**: औरनधाश ये चान्वे समन्त्मतस्य बरेष्टिता:। रेप सामनगृहणन्तु शिखशासनगौरवातू
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.3046)
- **Original**: जो भैरव आदि तथा दूसरे लोग जिवकों सब ओरसे घेरकर स्थित हैं, वे भी
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.3047)
- **Original**: 786 * संक्षिप्त सिवपुराण आदेशका गौरव मानकर सुझपर अनुप्ह करें
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.3048)
- **Original**: नारदाद्याक्ष मुत्यो दिव्या देवैश्व पूजिताः। साध्या गागाअ ये देवा जनसश्रेकनिजासिनः
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.3049)
- **Original**: वितिर्षुत्ताधिकाराक्ष महल्लेकिनियासिनः । सार्पयस्तथान्ये बे यैमानिकरगणैः सह
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.3050)
- **Original**: सर्वे. लिवार्धनरताः. शिवाज्ञावशयर्तिन:
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.3051)
- **Original**: दिवधोराज्या महां दिल्वन्तु ससकाह्षितम
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.3052)
- **Original**: नारद आदि देवपुजित साध्य, नाग, जनलोकनिवाली देवता, विदोषाधिकारसे सम्पन्न महत्वोंक-निवासी, सप्तर्षि तथा अन्य बैमानिकगण सदाशिबकी अच॑नामें तत्पर रहते हैं। ये सब शिवकी आज्ञाके अधीन हैं, अतः शिखा और जझिवकी आज्ञासे मुझे मनोबाव्छित वस्तु अदान करें
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.3053)
- **Original**: 173--175
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.3054)
- **Original**: ग््पर्याद्याः पिछाचान्ताशतस्रो टेवयोनम: । सिद्धा विद्याधराधाश्व ग्रेटपि चानये नधश्वरा:
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.3055)
- **Original**: असुरा॒ राक्षसाक्षेव पातालतलवापिन: । अननन्‍्ताद्याश नागेन्द्रा चैनतेकटयो द्विजा:
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.3056)
- **Original**: कृष्पाण्डा: प्रेललेताल्यथ ग्रह भूतगणा: पो। डाकिन्यश्वापियोगिन्‍्यः शाकिन्यश्वापि ताटुच्चा:
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.3057)
- **Original**: क्षेत्रगमगृदादीनि. तौर्थीन्यायतनानि च। ड्रीपा: समृद्रा नद्यश्ष नदाज्वान्य सरोसि च
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.3058)
- **Original**: गिरयश्न सुमेर्वाद्याः कहाननानि समनन्‍्ततः
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.3059)
- **Original**: पश्चव: पक्षिणो वृक्षा: कुमिकीटादयों मृगाः
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.3060)
- **Original**: आुलनात्यपि सर्वाणि भुवनानामभीक्षरा: । अण्डाय्यावरणै: साँ मासाक्ष दश दिग्गजाः
- **Translation**: 

---

