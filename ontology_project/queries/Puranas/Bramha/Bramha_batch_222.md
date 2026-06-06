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

### Verse 1 (Bramha 0.4421)
- **Original**: इस प्रकार इन्द्रकों फटकारकर उसने बारंबार किया; किंतु वरुण बड़े बुद्धिमान्‌ थे, उन्होंने
- **Translation**: 

---

### Verse 2 (Bramha 0.4422)
- **Original**: हँसते हुए कहा-“जाओ, जाओ; वरुणजीका महाशनिकों अपनी कन्या ब्याह दी। इधर तीनों
- **Translation**: 

---

### Verse 3 (Bramha 0.4423)
- **Original**: सदा आदर करना।' इन्द्र अपने घर आये। वे लोक बिना इन्द्रके हो गये। तब सब देवताओंने
- **Translation**: 

---

### Verse 4 (Bramha 0.4424)
- **Original**: अपमानपूर्ण लज्जासे काले पड़ गये थे। उन्होंने मिलकर सलाह की कि “भगवान्‌ विष्णु ही पुनः
- **Translation**: 

---

### Verse 5 (Bramha 0.4425)
- **Original**: शत्रुद्वार तिरस्कृत होनेकी सारी बातें इन्द्राणीको इन्द्रकों दे सकते हैं; क्योंकि बे ही दैत्योंके हन्ता
- **Translation**: 

---

### Verse 6 (Bramha 0.4426)
- **Original**: कह सुनायी और पूछा--'सुमुखि! शत्रुने मुझसे हैं। मन्त्रद्रष्टा भी वे ही हैं। अत: वे दूसरेको भी
- **Translation**: 

---

### Verse 7 (Bramha 0.4427)
- **Original**: इस तरह कठोर बातें कहीं और मेरे साथ ऐसा इन्द्र बना देंगे।' अनुचित बर्ताव किया। इससे मेरे हृदयमें आग ऐसा निश्चय करके सब देवता भगवान्‌ विष्णुके
- **Translation**: 

---

### Verse 8 (Bramha 0.4428)
- **Original**: लग रही है। तुम्हीं बताओ-- कैसे अपने हृदयको पास गये और उन्हें सब हाल कह सुनाया।
- **Translation**: 

---

### Verse 9 (Bramha 0.4429)
- **Original**: शीतल करूँ?' भगवान्‌ विष्णुने कहा--'महादैत्य महाशनि मेरे। . इन्द्राणीनी कहा--बलसूदन! मैं दानवॉकी लिये अवध्य है।' यों कहकर ये महाशनिके श्वशुर
- **Translation**: 

---

### Verse 10 (Bramha 0.4430)
- **Original**: उत्पत्ति, पराजय, माया, बरदान तथा मृत्यु-सब जरुणके पास गये और उन्हें इन्द्रके पराभवका
- **Translation**: 

---

### Verse 11 (Bramha 0.4431)
- **Original**: जानती हूँ। महाशनिको तपस्यासे ही यह शक्ति समाचार बतलाते हुए बोले--'तुम्हें ऐसा यत्न
- **Translation**: 

---

### Verse 12 (Bramha 0.4432)
- **Original**: प्राप्त हुई है। तपस्यासे कुछ भी असाध्य नहीं है। करना चाहिये, जिससे इन्द्र पुनः अपने पदपर
- **Translation**: 

---

### Verse 13 (Bramha 0.4433)
- **Original**: यज्ञ-कर्मसे कोई बात असम्भव नहीं है। जगन्नाथ लौट आयें।' भगवान्‌ विष्णुके आदेशसे वरुण
- **Translation**: 

---

### Verse 14 (Bramha 0.4434)
- **Original**: भगवान्‌ विष्णु तथा विश्वनाथ शिवकी भक्तिसे शौत्र ही वहाँ गये। दैत्यने विनयपूर्वक अपने
- **Translation**: 

---

### Verse 15 (Bramha 0.4435)
- **Original**: कोई भी कार्य ऐसा नहीं है, जो सिद्ध न हो अ्रशुरसे वहाँ पधारनेका कारण पूछा। वरुणने
- **Translation**: 

---

### Verse 16 (Bramha 0.4436)
- **Original**: सके ।* प्राणनाथ! मैंने और भी एक बहुत सुन्दर कहा--' महाबाहो ! कुछ दिन पहले तुमने इन्द्रको
- **Translation**: 

---

### Verse 17 (Bramha 0.4437)
- **Original**: बात सुन रखी है। कारण कि स्त्रियाँ ही परास्त करके रसातलमें बंदी बना लिया है। वे
- **Translation**: 

---

### Verse 18 (Bramha 0.4438)
- **Original**: स्त्रियोंके स्वभावको जानती हैं। प्रभो! भूमि तथा देवताओंके राजा हैं। उन्हें लौटा दो। यदि शत्रुको
- **Translation**: 

---

### Verse 19 (Bramha 0.4439)
- **Original**: जलकी अधिष्ठात्री देवियोंके द्वारा कोई भी कार्य बाँधकर फिर छोड़ दिया जाय तो वह सत्पुरुषोंके
- **Translation**: 

---

### Verse 20 (Bramha 0.4440)
- **Original**: असाध्य नहीं है। तपस्या अथवा यज्ञ आदि लिये महान्‌ कारण होता है।' “बहुत अच्छा'
- **Translation**: 

---

