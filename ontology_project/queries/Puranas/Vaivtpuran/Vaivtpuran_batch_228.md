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

### Verse 1 (Vaivtpuran 13.10702)
- **Original**: रचित सुरम्य तूलिकाओं, सुवर्णाकार मणियोंद्वारा देखकर सुन्दर नेत्रोंवाले श्रीकृष्णका ध्यान करके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10703)
- **Original**: निर्मित अत्यन्त सुन्दर सोपानों, लोहसारकी बनी वहाँ नगर-निर्माणका कार्य आरम्भ किया। हुई किवाड़ों तथा कृत्रिम चित्रोंसे वृषभानु- भारतवर्षका वह श्रेष्ठ और सुन्दर नगर पाँच
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10704)
- **Original**: भवनकी बड़ी शोभा हो रही थी। वहाँका प्रत्येक योजन विस्तृत था। तीर्थोंका सारभूत बह पुण्यक्षेत्र
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10705)
- **Original**: सुरम्य मन्दिर सोनेके कलशोंसे देदीप्यमान था। श्रीहरिको अत्यन्त प्रिय है। जो वहाँ मुमुक्षु होकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10706)
- **Original**: उस आश्रमके एक अत्यन्त मनोहर निर्जन प्रदेशमें, निवास करते हैं, उन्हें वह परम निर्वाणकी प्राप्ति जो मनोहर चम्पा-वृक्षोंके उद्यानके भीतर था, करानेवाला है। गोलोकमें पहुँचनेके लिये तो वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10707)
- **Original**: पतिसहित कलावतीके उपभोगके लिये विश्वकर्माने सोपानरूप है। सबको मनोबाज्छित वस्तु प्रदान कौतृहलवश एक ऐसी अपट्टालिका बनायी थी, करनेवाला है। वहाँ चार-चार कमरेवाले चार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10708)
- **Original**: जिसका निर्माण विशिष्ट श्रेणीकी श्रेष्ठ मणियोंद्वारा करोड़ भवन बनाये गये थे, जिससे वह नगर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10709)
- **Original**: हुआ था। उसमें इन्द्रनीलमणिके बने हुए नौ अत्यन्त मनोरम प्रतीत होता था। श्रेष्ठ प्रस्तरोंसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10710)
- **Original**: सोपान थे। गन्धसारनिर्मित खम्भों और कपाटोंसे निर्मित वह विशाल नगर किवाड़ों, खम्भों और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10711)
- **Original**: वह अत्यन्त ऊँचा मनोरम भवन सब ओरसे सोपानोंसे सुशोभित था। चित्रमयी पुत्तलिकाओं,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10712)
- **Original**: विलक्षण था। पुष्पों और कलशोंसे वहाँके भवनोंके शिखरभाग।. नारदजीने पूछा--भगवन्‌! मनोहर रूपवाली अत्यन्त प्रकाशमान जान पड़ते थे। पर्वतीय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10713)
- **Original**: कलावती कौन थी और किसकी पली थी, प्रस्तर-खण्डोंसे निर्मित वेदिकाएँ और प्राड्रण उस
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10714)
- **Original**: जिसके लिये देवशिल्पीने यलपूर्वक सुरम्य गृहका नगरके भवनोंकी शोभा बढ़ा रहे थे। प्रस्तर-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10715)
- **Original**: निर्माण किया? खण्डोंके परकोटोंसे सारा नगर घिरा हुआ था। भगवान्‌ नारायणने कहा--सुन्दरी कलावती विश्वकर्माने खेल-खेलमें ही सारे नगरकी रचना
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10716)
- **Original**: कमलाके अंशसे प्रकट हुई पितरोंकी मानसी कर डाली। प्रत्येक गृहमें यथायोग्य बड़े-छोटे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10717)
- **Original**: कन्या है और वृषभानुकी पतिक्रता पत्नी है। दो दरवाजे थे। हर्ष और उत्साहसे भरे हुए
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10718)
- **Original**: उसीकी पुत्री राधा हुईं जो श्रीकृष्णको प्राणोंसे देवशिल्पीने स्फटिक-जैसी मणियोंसे उस नगरके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10719)
- **Original**: भी बढ़कर प्रिय हैं। बे श्रीकृष्णे आधे अंशसे भवनोंका निर्माण किया था। गन्धसार-निर्मित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10720)
- **Original**: प्रकट हुई हैं; इसलिये उन्हींके समान तेजस्विनी सोपानों, शंकु-रचित खम्भों, लोहसारकी बनी हुई । हैं। उनके चरणकमलोंकी रजके स्पर्शसे बसुन्धरा किवाड़ों, चाँदीके समुज्ज्वल कलशों तथा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10721)
- **Original**: पवित्र हो गयी है। सभी संत-महात्मा सदा ही वज़सारनिर्मित प्राकारोंसे उस नगरकी अपूर्व शोभा
- **Translation**: 

---

