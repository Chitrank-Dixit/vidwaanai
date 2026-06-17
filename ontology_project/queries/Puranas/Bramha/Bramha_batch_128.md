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

### Verse 1 (Bramha 0.2541)
- **Original**: राज्यमें कुछ काल व्यतीत होनेके पश्चात्‌ एक
- **Translation**: 

---

### Verse 2 (Bramha 0.2542)
- **Original**: #ओं, -+ घटना घटित हुई। कपालगौतम नामक एक परम
- **Translation**: 

---

### Verse 3 (Bramha 0.2543)
- **Original**: 5) हा धर्मात्या ऋषि थे। उनके एक पुत्र हुआ, जो। दिल, कालवश दाँत निकलनेके पहले ही चल बसा।
- **Translation**: 

---

### Verse 4 (Bramha 0.2544)
- **Original**: 5222. उसे गोदमें लेकर बुद्धिमान्‌ ऋषि राजाके निकट
- **Translation**: 

---

### Verse 5 (Bramha 0.2545)
- **Original**: [9 आये। राजाने ऋषिकुमारकों अचेत अवस्थामें सोया
- **Translation**: 

---

### Verse 6 (Bramha 0.2546)
- **Original**: देख उसको जीवित करनेके लिये प्रतिज्ञा की। । राजा बोले--यदि यमलोकमें गये हुए इस,
- **Translation**: 

---

### Verse 7 (Bramha 0.2547)
- **Original**: +9,; के बालकको मैं सात दिनके भीतर न ला सकूँ तो
- **Translation**: 

---

### Verse 8 (Bramha 0.2548)
- **Original**: «>> 2“ 5 जलती हुई चितापर चढ़ जाऊँगा।
- **Translation**: 

---

### Verse 9 (Bramha 0.2549)
- **Original**: प्रसन्नता हुई। उन्होंने सब भूतोंकों भय देनेवाले यों कहकर राजाने लाख नीलकमलोंसे
- **Translation**: 

---

### Verse 10 (Bramha 0.2550)
- **Original**: कालको आज्ञा दी और कालने मृत्युके मुखमें पड़े महादेवजोौकी पूजा करके उनके मन्त्रका जप । हुए उस बालकको जीवित कर दिया। इसके बाद आरम्भ किया। जगदी श्वर भगवान्‌ शिव राजाकी
- **Translation**: 

---

### Verse 11 (Bramha 0.2551)
- **Original**: वे पार्वतीदेवीके साथ अन्तर्धान हो गये। अत्यन्त भक्तिका विचार करके पार्वतीजीके साथ
- **Translation**: 

---

### Verse 12 (Bramha 0.2552)
- **Original**: तदनन्तर राजाने हजारों वर्षोतक एकाग्रचित्त उनके सामने प्रकट हुए और बोले--'राजन्‌! मैं
- **Translation**: 

---

### Verse 13 (Bramha 0.2553)
- **Original**: होकर राज्य किया। फिर लौकिक धर्मों और तुमपर बहुत प्रसन्न हूँ।' महादेवजीका यह वचन
- **Translation**: 

---

### Verse 14 (Bramha 0.2554)
- **Original**: वैदिक नियमोंका विचार करके भगवान्‌ केशवको सुनकर राजा श्वेतने सहसा उनकी ओर देखा। वे
- **Translation**: 

---

### Verse 15 (Bramha 0.2555)
- **Original**: आराधनाका निश्चित ब्रत ग्रहण किया। इसके बाद सब अड्लोंमें भस्म रमाये हुए थे। उनके शरीरकी ' वे दक्षिणसमुद्रके पुरुषोत्तमक्षेत्रमें गये और जगन्नाथजीके कान्ति शरत्कालीन चन्द्रमा और कुन्दके समान
- **Translation**: 

---

### Verse 16 (Bramha 0.2556)
- **Original**: पास हो सुन्दर रमणीय प्रदेशमें एक सुन्दर मन्दिर थी। उनके नेत्र विकट थे। व्याप्नचर्मका वस्त्र और
- **Translation**: 

---

### Verse 17 (Bramha 0.2557)
- **Original**: बनवाया और श्वेतशिलाके द्वारा भगवान्‌ श्वेतमाधवको ललाटमें चन्द्रमाको रेखा थी। उनपर दृष्टि पड़ते । प्रतिमा बनवाकर विधिपूर्वक उसकी प्रतिष्ठा को। ही गाजाने सहसा पृथ्वीपर गिस्कर उन्हें प्रणाम किया
- **Translation**: 

---

### Verse 18 (Bramha 0.2558)
- **Original**: उस समय त्राह्मणों, दीनों, अना्थों और तपस्वियोंको और कहा--'प्रभो! यदि आप मुझपर प्रसन्न हैं, यदि दान दे राजाने भगवान्‌ माधवके समीप पृथ्वीपर आपकी मुझपर दया है तो कालके वशमें पड़ा हुआ
- **Translation**: 

---

### Verse 19 (Bramha 0.2559)
- **Original**: गिरकर साष्टाड़ प्रणाम किया। फिर एक मासतक यह ब्राह्मण-बालक पुनः जीवित हो जाय। यही मेरी
- **Translation**: 

---

### Verse 20 (Bramha 0.2560)
- **Original**: मौन एवं निराहर रहकर द्वादशाक्षर-मन्त्रका जप प्रतिज्ञा है। महे श्वर! आप इसे यथायोग्य आयुसे युक्त, किया। जप समाप्त होनेपर भगवान्‌ देवेश्वरकी इस और कल्याणका भागी बनायें।' [लिया आरम्भ की। श्रेवकी यह बात सुनकर महादेवजीको बड़ी
- **Translation**: 

---

