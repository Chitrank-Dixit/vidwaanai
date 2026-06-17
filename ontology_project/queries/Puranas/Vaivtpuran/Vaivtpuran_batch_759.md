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

### Verse 1 (Vaivtpuran 543.13494)
- **Original**: दे अपने धामको गये और प्रत्येक सभामें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13495)
- **Original**: 586 * संक्षिप्त ब्रह्मचैवर्तपुराण * अंक #ऋ ###### 668 64% #
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13496)
- **Original**: 4 ऋ ## 6944 5#####&#%$%%%%%%%ऊ कक पतिब्रताकी प्रशंसा करने लगे। पद्मा अपने तरुण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13497)
- **Original**: एकत्र की और उसके द्वारा महान्‌ यज्ञषका आयोजन पतिके साथ सदा एकान्तमें मिलन-सुखका अनुभव
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13498)
- **Original**: किया। उस यज्ञमें उन्होंने द्रेषषश शूलपाणि शंकरको करने लगी। पीछे उसके दस श्रेष्ठ पुत्र हुए जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13499)
- **Original**: भाग नहीं दिया। यह देख सतोके मनमें पिताके उसके पतिसे भी अधिक गुणवान्‌ थे। गिरिराज!
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13500)
- **Original**: प्रति बड़ा क्रोध हुआ। उसकी आँखें लाल हो गयीं। इस प्रकार मैंने सारा पुरातन इतिहास कह सुनाया।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13501)
- **Original**: उसने व्यधित-हृदयसे पिताको बहुत फटकारा और अनरण्यने अपनी पुत्री देकर समस्त सम्पत्तिकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13502)
- **Original**: यज्ञस्थानसे उठकर वह माताके पास गयी। उस रक्षा कर ली। तुम भी सबके ईश्वर भगवान्‌ परात्परा देवीकों तीनों कालोंका ज्ञान था; अतः शिवको अपनी कन्या देकर अपने समस्त यन्धुओं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13503)
- **Original**: उसने भविष्यमें घटित होनेवाली घटनाका वहाँ तथा सम्पूर्ण सम्पत्तिकी रक्षा करो। शैलराज! एक । वर्णन किया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13504)
- **Original**: यज्ञका विध्वंस, पिता दक्षका पराभव, सप्ताह बीतनेपर अत्यन्त दुर्लभ शुभ क्षणमें, जब
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13505)
- **Original**: यज्ञस्थानसे देवताओं, मुनियों, ऋत्विजों तथा पर्वतोंका चन्द्रमा लग्नेश होकर लग्नमें अपने पुत्र बुधके साथ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13506)
- **Original**: पलायन, शंकरके सैनिकोंकी विजय, अपनी मृत्यु, विराजमान होंगे; रोहिणीका संयोग पाकर प्रसन्नताका । पत्नौके विरहसे आतुर-चित्त होकर शोकबश पतिका अनुभव करते होंगे; चन्द्र और तारा सर्वथा शुद्ध
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13507)
- **Original**: पर्यटन, उनके नेत्रोंके जलसे सरोवरका निर्माण, होंगे; मार्गशीर्ष मासका सोमवार होगा; लग्र सब
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13508)
- **Original**: भगवान्‌ जनार्दनके समझानेसे उनका धैर्य धारण प्रकारके दोषोंसे रहित, समस्त शुभग्रहोंकी दृष्टिसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13509)
- **Original**: करना, दूसरे शरीरसे पुनः शिवकी प्राप्ति, उनके लक्षित और असत्‌ ग्रहोंसे शून्य होगा; उत्तम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13510)
- **Original**: साथ विहार तथा अन्य सब भावी वृत्तान्त बताकर संतानप्रद, पतिसौभाग्यदायक, चैधव्यनिवारक, जन्म-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13511)
- **Original**: सती माता और बहनोंके मना करनेपर भी दुःखी जन्ममें सुख प्रदान करनेवाला तथा प्रेमका कभी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13512)
- **Original**: हो घेर्से चली गयी। वह सिद्धयोगिनी थी। अतः विच्छेद न होने देनेवाला अत्यन्त श्रेष्ठटम योग
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13513)
- **Original**: योगबलसे सबकी दृष्टिसे ओझल हो गयी ।गड्भाजीके उपस्थित होगा; उस समय तुम अपनी पुत्री
- **Translation**: 

---

