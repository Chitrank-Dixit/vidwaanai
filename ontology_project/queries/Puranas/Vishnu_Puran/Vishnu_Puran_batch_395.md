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

### Verse 1 (Vishnu Puran 0.7881)
- **Original**: तस्यैवज्भुणमिथुनादुत्पत्ति:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7882)
- **Original**: तत्कथ- मस्मिन्नपक्रान्तेडत्र॒ दुर्भिक्षमारिकाडुपद्रवा ने भ्रविष्यन्ति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7883)
- **Original**: तदयमत्रानीयतामलछमति- कृतापराधतितिक्षृभिरभय दत्त्वा ध्रफल्कपुत्र: स्वपुर- मानीतः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7884)
- **Original**: तत्र चागतमात्र एवं तस्य स्थमन्तकमणे: प्रभावादनावृष्टिमारिकादुर्भिक्ष- व्यालाद्युपद्रवोपशमा बभूवु:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7885)
- **Original**: कृष्णश्चिन्तयामास
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7886)
- **Original**: स्वल्पमेतत्‌- कारणं यदयं गान्दिन्यां श्रफल्केनाक्रूरों जनितः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7887)
- **Original**: सुमहांश्रायमनावृष्टिदुर्भिक्ष- प्रभाव:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7888)
- **Original**: तच्चूनमस्य सकाहे स महामणि: स्थमन्तकाख्य- स्तिष्ठति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7889)
- **Original**: तस्य ह्ोयंबिधा: प्रभावा: श्रूयन्ते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7890)
- **Original**: अयमपि च॒ यज्ञादनन्तर- आओविष्णुपुराण ( अ« 13 लगी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7891)
- **Original**: उस समय काहिराजकी रानीके गर्भमें एक कन्यारत्र थो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7892)
- **Original**: कह कन्या प्रसृतिकालके समाप्त होनेपर भी गर्भसे बाहर न आयी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7893)
- **Original**: इस प्रकार उस गर्भको प्रसन दुए बिना बारह वर्ष व्यतीत हो गये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7894)
- **Original**: तब काहिराजने अपनी उस गर्भस्थिता पुत्रीसे कहा--
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7895)
- **Original**: 'बेटी ! तू उत्पन्न क्यों नहीं होती ? बाहर आ, मैं तेश सुख देखना चाहता हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7896)
- **Original**: अपनी इस माताकों तू इतने दिनोंसे क्यों कष्ट दे रही है ?' राजाके ऐसा कहनेपर उसते गर्भमें रहते हुए ही कहा---'पिताजी ! यदि आप प्रतिदिन एक गौ ब्राह्मणको दान देंगे तो अगछे तीन वर्ष बीतनेपर मैं अवश्य गर्भसे बाहर आ जाऊँगी ।' इस खातकों सुनकर राजा अतिदिन ब्राह्मणक्रों एक गौ देने लो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7897)
- **Original**: तव उतने समय (तीन वर्ष) बीतनेपर बह ढत्पन्न हुई
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7898)
- **Original**: पिताने उसका नाम गान्दिनी रखा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7899)
- **Original**: और उसे अपने उफ्कारक श्वफल्कको, घर आनेपर अर्थ्यरूपसे दे दिया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7900)
- **Original**: उसीसे श्रफल्कके द्वाग इन अक्रूस्जोका जन्म हुआ है
- **Translation**: 

---

