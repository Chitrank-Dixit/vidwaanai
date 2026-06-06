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

### Verse 1 (Vaivtpuran 63.5520)
- **Original**: हैं। उनका मुख सुन्दर एवं गोलाकार है। वे नारद! तत्पश्चात्‌ देवीके सामने कलशपर गणेश,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5521)
- **Original**: भगवान्‌ शिवके मनको मोहनेवाली हैं। रत्रोंके सूर्य, अग्नि, विष्णु, शिव और पार्वती-इन छ:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5522)
- **Original**: युगल कुण्डलसे उनके कपोल उद्धासित होते देवताओंका आवाहन करके राजाने विधिपूर्वक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5523)
- **Original**: रहते हैं। वे नासिकाके दक्षिण भागमें गजमुक्तासे भक्तिसे उनका पूजन किया। प्रत्येक विद्वान्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5524)
- **Original**: निर्मित नथ धारण करती हैं। कानोंमें बहुसंख्यक पुरुषको चाहिये कि वह पूर्बोक्त छः देवताओंकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5525)
- **Original**: बहुमूल्य रत्रमय आभूषण पहनती हैं। मोतियोंकी पूजा और बन्दना करके महादेबीका प्रेमपूर्वक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5526)
- **Original**: पाँतको तिरस्कृत करनेवाली दन्तपंक्ति उनके मुखकी निम्नाद्धित रीतिसे ध्यान करे। मुने! सामवेदमें जो शोभा बढ़ाती है। पके हुए बिम्बफ़लके समान ध्यान बताया गया है, वह परम उत्तम तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5527)
- **Original**: उनके लाल-लाल ओठ हैं। वे अत्यन्त प्रसन्न तथा कल्पवृक्षके समान वाञ्छापूरक है। परम मड्भजलमयी हैं। विचित्र पत्ररचनासे रमणीय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5528)
- **Original**: 286 * संक्षितत स्ह्मवैचर्तपुराण « ऋकऋ%ऋ 24 44]]]440 0 0 4 6 62.6 2944 44444 4
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5529)
- **Original**: 4)]।]]0]4084844 24 5 4
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5530)
- **Original**: 3 6 4 22 92.24
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5531)
- **Original**: उनके कपोल-युगल परम उज्ज्वल प्रतीत होते हैं।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5532)
- **Original**: हिरण्यकशिपुके वधकालमें ये नृसिंहशक्तिरूपमें रत्रोंके बने हुए बाजूबन्द, कंगन तथा रत्रमय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5533)
- **Original**: प्रकट हुई थीं। हिरण्याक्षके वधकालमें भगवान्‌ मजञजर उनके विभिन्न अज्जोंका सौन्दर्य बढ़ाते हैं। वाराहक॑ भीतर वाराही शक्ति यहीं थीं। ये र्मय कह्कूणोंसे उनके दोनों हाथ विभूषित हैं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5534)
- **Original**: परब्रह्मरूपिणी तथा सर्वशक्तिस्वरूपा हैं। मैं सदा रज्रमय पाशक उनकी शोभा बढ़ांते हैं। रत्रमयी [इनका भजन करता हूँ। अंगूठियोंसे उनके हाथोंकी अँगुलियाँ जगमगाती इस प्रकार ध्यान करके विद्वान्‌ पुरुष अपने रहती हैं। पैरोंकी अँगुलियोंक और नखोंमें लगे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5535)
- **Original**: सिरपर पुष्प रखे और पुनः ध्यान करके हुए महावरकी रेखा उनकी शोभावृद्धि करती है।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5536)
- **Original**: भक्तिभावसे आवाहन करे। प्रकृतिकी प्रतिमाका वे अग्निशुद्ध दिव्य वस्त्र धारण करती हैं। उनके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5537)
- **Original**: स्पर्श करके मनुष्य इस प्रकार मन्त्र पढ़े तथा विभिन्न अद्भ गन्ध, चन्दनसे चर्चित हैं। वे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5538)
- **Original**: मन्त्रद्वारा ही यत्रपूर्वक्ष जीव-न्यास करे। कस्तूरीके विन्दुओंसे सुशोभित दो स्तन धारण अम्ब! भगवति! सनातनि! शिवलोकसे करती हैं। सम्पूर्ण रूप और गुणोंसे सम्पन्न हैं तथा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5539)
- **Original**: आओ, आओ । सुरेश्वरि ! मेरी शारदीया पूजा ग्रहण गजराजके समान मन्द गतिसे चलती हैं। अत्यन्त
- **Translation**: 

---

