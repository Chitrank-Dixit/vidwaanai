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

### Verse 1 (Vaivtpuran 13.10862)
- **Original**: निर्माण किया, जो सब ओरसे एक-एक योजन छ4 4 5.
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10863)
- **Original**: डटड * संक्षिप्त ब्रह्मवैवर्तपुराण « विस्तृत था। उसमें स्थान-स्थानपर मणिमय
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10864)
- **Original**: शोभा बढ़ा रहे थे। उसमें सब ओर अमूल्य रत्रमय बेदिकाएँ बनी हुई थीं। मणिसाररचित नौ करोड़
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10865)
- **Original**: दर्पण लगे थे, जिनके कारण सबको अपने मण्डप उस रासमण्डलकी शोभा बढ़ाते थे। वे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10866)
- **Original**: सामनेकी ओरसे ही वह मण्डप दीप्तिमान्‌ दिखायी श्रृज्ञारके योग्य, चित्रोंसे सुसज्जित और शब्याओंसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10867)
- **Original**: देता था। वह सौ धनुष ऊपरतक अग्रि-शिखाके सम्पन्न थे। नाना जातिके फूलोंकी सुगन्‍्ध लेकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10868)
- **Original**: समान प्रकाशपुझ फैला रहा था। उसका विस्तार बहती हुई वायु उन मण्डपोंको सुवासित करती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10869)
- **Original**: सौ हाथका था। वह रल्लमण्डप गोलाकार बना था। थी। उनमें रत्रमय प्रदीप जलते थे। सुवर्णमय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10870)
- **Original**: उसके भीतर रल्ननिर्मित शय्याएँ बिछी थीं, जिनसे कलश उनकी उज्वलता बढ़ा रहे थे। पुष्पोंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10871)
- **Original**: उस उत्तम भवनके भीतरी भागकी बड़ी शोभा हो भरे हुए उद्यानों तथा सरोबरोंसे सुशोभित रही थी। उक्त शय्याओंपर अग्निशुद्ध दिव्य वस्त्र रासस्थलका निर्माण करके विश्वकर्मा दूसरे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10872)
- **Original**: बिछे थे। मालाओंके समूहसे सुसज्जित होकर वे स्थानको गये। वे उस रमणीय बृन्दावनको देखकर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10873)
- **Original**: विचित्र शोभा धारण करते थे। पारिजातके फूलोंकी बहुत संतुष्ट हुए। वनके भीतर जगह-जगह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10874)
- **Original**: मालाओंके बने हुए तकिये उनपर यथास्थान रखे एकान्त स्थानमें मन-बुद्धिसे विचार और निश्चय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10875)
- **Original**: गये थे। चन्दन, अगुरु, कस्तूरी और कुंकुमसे वह करके उन्होंने वहाँ तीस रमणीय एवं विलक्षण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10876)
- **Original**: सारा भवन सुवासित हो रहा था। उसमें मालती वनोंका निर्माण किया। वे केवल श्रीराधा-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10877)
- **Original**: और चम्पाके फूलोंकी मालाएँ रखी थीं। नूतन माधवकी ही क्रौड़ाके लिये बनाये गये थे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10878)
- **Original**: श्रृज्धारेक योग्य तथा पारस्परिक प्रेमकी वृद्धि तदनन्तर मधुवनके निकट अत्यन्त मनोहर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10879)
- **Original**: करनेवाले कपूरयुक्त ताम्बूलके बीड़े उत्तम रत्रमय निर्जन स्थानमें बटबृक्षेके मूलभागके निकट सरोवरके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10880)
- **Original**: पात्रोंमें सजाकर रखे गये थे। उस भवनमें रत्नोंकी पश्चिम किनारे केतकीवनके बीच और चम्पाके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10881)
- **Original**: बनी हुई बहुत-सी चौकियाँ थीं, जिनमें हीरे जड़े उद्यानके पूर्व विश्वकर्मने राधा-माधवकी क्रौड़ाके
- **Translation**: 

---

