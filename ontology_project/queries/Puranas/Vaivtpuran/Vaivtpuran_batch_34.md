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

### Verse 1 (Vaivtpuran 4.8576)
- **Original**: + गणपतिखण्ड « 397 5#&4#%$$ 86 56448 554 446 85454 # 44644 46644 44484 48 48 88444 848 4 85 8 # ऊ 4 5 $ 5 # / 4555 45 5. और निराहार रहकर वहाँ दीर्घकालिक तपस्यामें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8577)
- **Original**: फलकी प्राप्ति होती है। पुत्रहीन मनुष्य श्रीगणेशको संलग्न हो गयी। नारद! तत्पश्चात्‌ मुनिवरके तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8578)
- **Original**: कृपासे धीर, वीर, धनी, गुणी, चिरजीवी, गणेशके शापसे वह चिरकालतक शक्लुचूडकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8579)
- **Original**: यशस्वी, पुत्रबान्‌, विद्वान, श्रेष्ठ कवि, जितेन्द्रियोंमें प्रिय पत्नी बनी रही। मुने! तदनन्तर असुरराज
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8580)
- **Original**: श्रेष्ठ समस्त सम्पदाओंका दाता, परम पतित्र, शब्डुचूड शंकरजीके त्रिशूलसे मृत्युको प्राप्त हो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8581)
- **Original**: सदाचारी, प्रशंसनीय, विष्णुभक्त, अहिंसक, दयालु गया, तब नारायणप्रिया तुलसी कलांशसे वृक्षभावको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8582)
- **Original**: और तत्त्वज्ञानविशारद पुत्र पाता है। महावन्ध्या प्राप्त हो गयी। यह इतिहास, जिसका मैंने तुमसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8583)
- **Original**: स्त्री वस्त्र, अलंकार और चन्दनद्वारा भक्तिपूर्वक वर्णन किया है, पूर्वकालमें धर्मके मुखसे सुना
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8584)
- **Original**: गणेशकी पूजा करके और इस गणपतिखण्डको था। इसका वर्णन अन्य पुराणोंमें नहीं मिलता।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8585)
- **Original**: सुनकर पुत्रको जन्म देती है। जो मनुष्य यह तत्त्वरूप तथा मोक्ष प्रदान करनेवाला है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8586)
- **Original**: नियमपरायण हो मनमें किसी कामनाकों लेकर तदनन्तर महाभाग परशुराम गणेशका पूजन करके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8587)
- **Original**: इसे सुनता है, सुरश्रेष्ठ गणेश उसकी सभ॑। तथा शंकर और पार्वतीको नमस्कार कर तपस्याके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8588)
- **Original**: कामनाएँ पूर्ण कर देते हैं। विध्ननाशके लिये लिये वनको चले गये। इधर गणेश समस्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8589)
- **Original**: यत्रपूर्वक इस गणपतिखण्डको सुनकर वाचकको सुरश्रेष्ठों तथा मुनिवरोंसे वन्दित एवं पूजित होकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8590)
- **Original**: सोनेका यज्ञोपवीत, श्वेत छत्र, श्वेत अश्व, श्वेतपुष्पोंकी शिव-पार्वतीके निकट स्थित हुए। माला, स्वस्तिक मिष्टान्न, तिलके लड्डू और जो मनुष्य इस गणपति-खण्डको दत्तचित्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8591)
- **Original**: देशकालोद्भव पके हुए फल प्रदान करना चाहिये। होकर सुनता है, उसे निश्चय ही राजसूययज्ञके (अध्याय 46) नि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8592)
- **Original**: गणपतिखण्ड सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8593)
- **Original**: 8-7 मग्पप20-> जन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8594)
- **Original**: नारदजीके प्रश्न तथा मुनिवर नारायणद्वारा भगवान्‌ विष्णु एवं वैष्णवके माहात्म्यका वर्णन, श्रीराधा और श्रीकृष्णके गोकुलमें अवतार लेनेका एक कारण श्रीदाम और राधाका परस्पर शाप नारायण नमस्कृत्य नरें चैब नरोत्तमम्‌।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8595)
- **Original**: अंशोंसे इस भूतलपर अवतीर्ण हुए? किस युगमें, देवीं सरस्वती चैब ततो जयमुदीरयेत्‌
- **Translation**: 

---

