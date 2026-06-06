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

### Verse 1 (Mahabharat 0.961)
- **Original**: पेड़की छालके बस्ध और मृगचर्म धारण कर बह अपने पतिके विचार किया कि बंशपरम्पराका उद्ेद न हो, इसलिये वियाह
- **Translation**: 

---

### Verse 2 (Mahabharat 0.961)
- **Original**: पेड़की छालके बस्ध और मृगचर्म धारण कर बह अपने पतिके विचार किया कि बंशपरम्पराका उद्ेद न हो, इसलिये वियाह
- **Translation**: 

---

### Verse 3 (Mahabharat 0.962)
- **Original**: समान ही व्रत और नियमोंका पालन करने लगी। तदसत्तर करना आवश्यक है। किंतु उत्हें कोई भी ख्री अपने अनुरूप
- **Translation**: 

---

### Verse 4 (Mahabharat 0.962)
- **Original**: समान ही व्रत और नियमोंका पालन करने लगी। तदसत्तर करना आवश्यक है। किंतु उत्हें कोई भी ख्री अपने अनुरूप
- **Translation**: 

---

### Verse 5 (Mahabharat 0.963)
- **Original**: भगवान्‌ अगस्त्य हरिद्वार क्षेत्र आकर अपनी अनुगता न जान पड़ी। तब उन्होंने विदर्भ देशके राजाके पास जाकर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.963)
- **Original**: भगवान्‌ अगस्त्य हरिद्वार क्षेत्र आकर अपनी अनुगता न जान पड़ी। तब उन्होंने विदर्भ देशके राजाके पास जाकर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.964)
- **Original**: भायाके सहित घोर तपस्या करने लूगे। ल्तोपामुद्रा बड़े ही प्रेम कहा “राजन ! पुत्रोत्पत्तिकी इच्छासे मेरा विचार विवाह
- **Translation**: 

---

### Verse 8 (Mahabharat 0.964)
- **Original**: भायाके सहित घोर तपस्या करने लूगे। ल्तोपामुद्रा बड़े ही प्रेम कहा “राजन ! पुत्रोत्पत्तिकी इच्छासे मेरा विचार विवाह
- **Translation**: 

---

### Verse 9 (Mahabharat 0.965)
- **Original**: और तत्परतासे अपने पतिदेवकी सेवा करती थी तथा करनेका है। इसलिये मैं आपसे आपकी पुत्री स्पेपामुद्रको
- **Translation**: 

---

### Verse 10 (Mahabharat 0.965)
- **Original**: और तत्परतासे अपने पतिदेवकी सेवा करती थी तथा करनेका है। इसलिये मैं आपसे आपकी पुत्री स्पेपामुद्रको
- **Translation**: 

---

### Verse 11 (Mahabharat 0.966)
- **Original**: भगवान्‌ अगस््वजी भी अपनी भावाके साथ बड़े प्रेमका माँगता हूँ। आप मेरे साथ इसका विवाह कर दें।! बर्ताव करते थे। /'मुनियर अगस्यकी यह जात सुनकर राजाके होझ उड़
- **Translation**: 

---

### Verse 12 (Mahabharat 0.966)
- **Original**: भगवान्‌ अगस््वजी भी अपनी भावाके साथ बड़े प्रेमका माँगता हूँ। आप मेरे साथ इसका विवाह कर दें।! बर्ताव करते थे। /'मुनियर अगस्यकी यह जात सुनकर राजाके होझ उड़
- **Translation**: 

---

### Verse 13 (Mahabharat 0.967)
- **Original**: ““राजन्‌ ! जब इसी प्रकार बहुत समय निकल गया: तो गये । बे न तो अस्वीकार ही कर सके और न कन्या देमेका
- **Translation**: 

---

### Verse 14 (Mahabharat 0.967)
- **Original**: ““राजन्‌ ! जब इसी प्रकार बहुत समय निकल गया: तो गये । बे न तो अस्वीकार ही कर सके और न कन्या देमेका
- **Translation**: 

---

### Verse 15 (Mahabharat 0.968)
- **Original**: एक दिन मुनिबर अगसरूयने ऋतुख्ानसे निवृत्त हुई साहस . ही ।. उन्होंने महारानीके पास जा उन्हें सब वृत्तात्त
- **Translation**: 

---

### Verse 16 (Mahabharat 0.968)
- **Original**: एक दिन मुनिबर अगसरूयने ऋतुख्ानसे निवृत्त हुई साहस . ही ।. उन्होंने महारानीके पास जा उन्हें सब वृत्तात्त
- **Translation**: 

---

### Verse 17 (Mahabharat 0.969)
- **Original**: ल्लेपासुद्राको देखा । इस समय तपके अभावसे उसकी कान्ति सुनाकर कहा, 'प्रिये ! महर्षि अगस़््य बड़े हो तेजस्वी हैं। वे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.969)
- **Original**: ल्लेपासुद्राको देखा । इस समय तपके अभावसे उसकी कान्ति सुनाकर कहा, 'प्रिये ! महर्षि अगस़््य बड़े हो तेजस्वी हैं। वे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.970)
- **Original**: बहुत बड़ी हुई थी। उसकी सेवा, पवित्रता, संयम, कात्ति क्रोधित हो गये तो हमें झापकौ भयानक आगसे भस्म कर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.970)
- **Original**: बहुत बड़ी हुई थी। उसकी सेवा, पवित्रता, संयम, कात्ति क्रोधित हो गये तो हमें झापकौ भयानक आगसे भस्म कर
- **Translation**: 

---

