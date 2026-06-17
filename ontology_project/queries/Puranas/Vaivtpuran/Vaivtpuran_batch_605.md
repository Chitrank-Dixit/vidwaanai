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

### Verse 1 (Vaivtpuran 53.4934)
- **Original**: धर 2 08000 39.48 4! /9ऐ पं आधी लंबाई-चौड़ाई तथा शतश्ृज्ग पर्वतकी आधी है 9, 1 3/(4 2 2 52268 ऊँचाईवाले वृन्दावनसे वह धाम सुशोभित है। रत हृ ड़ )
- **Translation**: 

---

### Verse 2 (Vaivtpuran 53.4935)
- **Original**: 6 वृन्दावनकी अपेक्षा आधी लंबाई-चौड़ाईमें निर्मित 70/220:/ गोलोकधामका अलंकार है। उपर्युक्त है 56520 233 54828, [रासमण्डल * मका 8 नदी, पर्वत और वन आदिके मध्यभागमें मुख्य गोलोकधाम है। जैसे कमलमें कर्णिका होती है,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 53.4936)
- **Original**: उसी प्रकार उक्त नदी, शैल आदिके बीचमें वह - - -+-+ मनोहर धाम प्रतिष्ठित है। वहाँ रासमण्डलमें वह अलक्ष्य तथा आश्रयरहित है। आकाशके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 53.4937)
- **Original**: गौओं, गोपों और गोपियोंसे घिरे हुए गोपीवल्लभ समान अत्यन्त विस्तृत तथा अमूल्य दिव्य र्रोंद्वारा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 53.4938)
- **Original**: श्रीकृष्ण रासेश्वरी श्रीराधाके साथ निरन्तर निवास निर्मित है। वहाँ वनमालाधारी श्रीमान्‌ चतुर्भुज
- **Translation**: 

---

### Verse 6 (Vaivtpuran 53.4939)
- **Original**: करते हैं। उनके दो भुजाएँ हैं, वे हाथोंमें मुरली नारायणदेव, जो लक्ष्मी, सरस्वती, गड्भा तथा लिये बाल-गोपालका रूप धारण किये रहते हैं। तुलसीके पति हैं; सुनन्द, नन्‍द तथा कुमुद आदि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 53.4940)
- **Original**: अग्निशुद्ध चिन्मय वस्त्र उनका परिधान है। वे पार्षदोंसे घिरे हुए निवास करते हैं। रत्रमय आभूषणोंसे विभूषित हैं। उनके सारे अज्ज सर्वेश्वर, सर्वसिद्धेश्वर एवं भक्तोंपर अनुग्रह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 53.4941)
- **Original**: चन्दनसे चर्चित हैं। गलेमें रज्नोंका हार शोभा देता करनेके लिये ही दिव्य विग्रह (अथवा कृपामय
- **Translation**: 

---

### Verse 9 (Vaivtpuran 53.4942)
- **Original**: है। वे रत्रमय सिंहासनपर विराजमान हैं। उनके शरीर) धारण करनेवाले भगवान्‌ श्रीकृष्ण दो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 53.4943)
- **Original**: ऊपर रज्नरमय छत्र तना हुआ है तथा उनके प्रिय रूपोमें प्रकट हैं--द्विभुज एवं चतुर्भुज
- **Translation**: 

---

### Verse 11 (Vaivtpuran 53.4944)
- **Original**: चतुर्भुजरूपसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 53.4945)
- **Original**: सखा ग्वालबाल श्वेत चवौर लिये सदा उनकी बे वैकुण्ठमें वास करते हैं और द्विभुजरूपसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 53.4946)
- **Original**: सेवामें तत्पर रहते हैं। वस्त्राभूषणोंसे विभूषित गोलोकधाममें। बैकुण्ठसे पचास करोड़ योजन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 53.4947)
- **Original**: सुन्दर बेषवाली गोपियाँ माला और चन्दनके द्वारा ऊपर गोलाकार “गोलोक 'धाम विद्यमान है, जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 53.4948)
- **Original**: उनका श्रृज्ञार करती हैं। वे मन्द-मन्द मुस्कराते समस्त लोकोंसे श्रेष्ठठटम है। बहुमूल्य रत्रोंड्वारा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 53.4949)
- **Original**: रहते हैं और बे गोपियाँ कटाक्षपूर्ण चितबनसे निर्मित विशाल भवन उस धामकी शोभा बढ़ाते उनकी ओर निहारती रहती हैं। हैं। र्लेनद्रसाके बने हुए विचित्र खम्भों और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 53.4950)
- **Original**: इस प्रकार जैसा मैंने भगवान्‌ शंकरके मुखसे सीढ़ियोंसे वे भवन अलंकृत हैं। श्रेष्ठ मणिमय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 53.4951)
- **Original**: सुना था और आममोंमें जैसा वर्णव मिलता है, दर्पणोंसे जटित किवाड़ों तथा कलशोंसे उज्ज्वल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 53.4952)
- **Original**: तदनुसार लोकविस्तारकी यथाशक्ति चर्चा को है। एवं नाना प्रकारके चित्रोंसे विचित्र शोभा पानेवाले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 53.4953)
- **Original**: अब कालका मान सुनो। छ: पल सोनेका बना शिविर उस धामकी अश्रीवृद्धि करते हैं। उसका
- **Translation**: 

---

