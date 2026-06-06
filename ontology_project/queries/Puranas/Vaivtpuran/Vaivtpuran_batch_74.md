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

### Verse 1 (Vaivtpuran 6.9291)
- **Original**: सबको बड़ा विस्मय हुआ। सारतत्त्वके बने हुए मझीर अपनी मधुर झनकार
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9292)
- **Original**: श्वेतद्वीपनिवासी श्रीविष्णुके श्रीकृष्णविग्रहमें फैला रहे थे। पारिजातके फूलोंकी मालाओंसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9293)
- **Original**: विलीन हो जानेके बाद वहाँ तुरंत ही शुद्ध
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9294)
- **Original**: ] श्रीकृष्णजन्मरवण्ड # डर9 ऋडऋकऋकऋ%ऋ कं ##ऋ$%ऋऋऋऋऋ$%कऋऋऊऋ$ऋऊऋऋऊऋड कक ############&######### स्फटिकमणिके समान गौरवर्णवाले संकर्षण नामक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9295)
- **Original**: सारभागकी प्रभाका अपहरण कर रही थीं। उन पुरुष पधारे। वे बड़ी उतावलीमें थे। उनके सहस्नों
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9296)
- **Original**: अनुपम तेजःस्वरूपा देवीके सहस्नों भुजाएँ थीं मस्तक थे तथा वे सौ सूर्योंके समान देदीप्यमान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9297)
- **Original**: और उनमें भाँति-भातिके आयुध शोभा पा रहे थे। हो रहे थे। उनको आया देख सबने उन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9298)
- **Original**: उनके प्रसन्न मुखपर मन्द हासकी छटा छा रही विष्णुस्वरूप संकर्षणका स्तवन किया। नारद!
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9299)
- **Original**: थी। वे भक्तोंपर कृपा करनेके लिये कातर उन्होंने भी वहाँ आकर मस्तक झुकाकर राधिकेश्वरकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9300)
- **Original**: दिखायी देती थीं। उनके गण्डस्थल और कपोल स्तुति की तथा सहस्नों मस्तकोंद्वारा भक्तिभावसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9301)
- **Original**: उत्तम रत्रमय कुण्डलोंसे उद्धासित हो रहे थे। उनको प्रणाम किया। तत्पश्चात्‌ धर्मके पुत्र-स्वरूप
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9302)
- **Original**: रत्रेद्रसाररचित तथा मधुर झनकारसे युक्त मआजरोंके हम दोनों भाई नर और नारायण वहाँ गये। मैं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9303)
- **Original**: कारण उनके चरणोंकी अपूर्व शोभा हो रही थी। तो श्रीकृष्णके चरणारविन्दमें लीन हो गया। किंतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9304)
- **Original**: श्रेष्ठ मणिनिर्मित मेखलासे मण्डित मध्यदेश अत्यन्त नर अर्जुनके रूपमें दृष्टिगोचर हुआ। फिर ब्रह्मा,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9305)
- **Original**: मनोहर दिखायी देता था। हाथोंमें श्रेष्ठ रलसारके शिव, शेष और धर्म--ये चारों वहाँ एक स्थानपर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9306)
- **Original**: बने हुए केयूर और कड्भूण शोभा दे रहे थे। खड़े हो गये। मन्दार-पुष्पोंकी मालाओंसे अलंकृत वक्ष:स्थल इस बीचमें देवताओंने वहाँ दूसरा उत्तम रथ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9307)
- **Original**: अत्यन्त उज्ज्वल जान पड़ता था। शरत्कालके देखा, जो सुवर्णके सारतत्त्वका बना हुआ था और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9308)
- **Original**: सुधाकरकी आभाको तिरस्कृत करनेवाले सुन्दर नाना प्रकारके रज्ञनिर्मित उपकरणोंसे अलंकृत था।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9309)
- **Original**: मुखसे उनकी मनोहरता और बढ़ गयी थी। वह श्रेष्ठ मणियोंके सारतत्त्वसे संयुक्त, अग्निशुद्ध / काजलकी काली रेखासे युक्त नेत्र शरत्कालके दिव्य वस्त्रसे सुसज्जित, श्वेत चँवर तथा दर्पणोंसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9310)
- **Original**: प्रफुल्ल नील कमलोंकी शोभाको लज्जित कर रहे अलंकृत, सद्रत्न-सारनिर्मित कलश-समूहसे
- **Translation**: 

---

