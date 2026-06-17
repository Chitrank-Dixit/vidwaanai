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

### Verse 1 (Vishnu Puran 0.7481)
- **Original**: और निरन्तर भोगते रहनेसे उन कासनाओंकों अत्यन्त प्रिय सानने छरे; तदुपरान्त उन्होंने इस प्रकार अपया उद्धार प्रकट किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7482)
- **Original**: अल्कि घृताहुतिसे अग्रिके समान बह बढ़ती ही जाती है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7483)
- **Original**: सम्पूर्ण पृथिवीमें जितने भी धान्य, यब, सुबर्ण, पशु और स्त्रियां हैं वे सब एक मनुष्यके लिये भी सन्तोषजनक नहीं हैं, इसलिये तृष्णाको सर्वथा त्याग देना चाहिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7484)
- **Original**: जिस समय कोई पुरुष किसी भी ग्राणीके लिये पापमयों भाषना नहीं करता उस समय उस समद्शके लिये सभी दिद्ाएँ सुखमयी हो जाती हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7485)
- **Original**: दुर्मतियोंके लिये जो अत्यन्त दुस्त्यज है तथा जुद्धावस्थार्में भी जो शिथिल नहीं होती, बुद्धिमान पुरुष उस तृष्णाको त्यागकर सुखसे परिपूर्ण हो जाता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7486)
- **Original**: अच्स्थाके जीर्ण होनेपर केश और दाँत तो जोर्ण हो जाते हैं किन्तु जीवन और ध्नकी आज्ञाएँ उसके जीर्ण होनेपर भी नहीं जीर्ण होतीं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7487)
- **Original**: बिषयोंमें आसक्त रहते हुए मुझे एक सहस्त्र वर्ष जीत गये, फिर भी निस्य डी उनमें मेरी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7488)
- **Original**: 246 तस्मादेतामहं त्यक्त्वा ब्रह्मणयाधाय मानसम्‌ । निईन्द्दो निर्ममो भूत्वा चरिष्यामि मृगैस्सह
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7489)
- **Original**: 29 आपराशर उताच पूरोस्सकाझादादाय जरां दत््वा च यौवनम्‌ राज्येडभिषिच्य पूरुं चर प्रययौ तपसे वनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7490)
- **Original**: 30 दिशि दक्षिणपूर्वस्यां तुर्वसं च समादिह्वत्‌ । प्रतीच्यां च तथा बुह्मुं दक्षिणायां ततो यदुम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7491)
- **Original**: 31 उदीच्यां च तथैवानु कृत्वा पण्डलिनो नृपान्‌ । श्रीविष्णुपुराण [ अष् 11 क्यमना होतो है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7492)
- **Original**: अतः अब मैं इसे छोड़कर और अपने चित्तको भगवानमें ही स्थिरवर निर्दन्द्र और निर्मम होकर [ कनमें ] मृगोंके साथ बिचरूँगा'
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7493)
- **Original**: श्रीपराझरजी बोले--तदनन्तर राजा ययातिने पूरुसे अपनी वृद्धावस्था छेकर उसका सौवन दे दिया और ठसे राज्य-्पदपर अभिषिक्त कर बनको चले गये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7494)
- **Original**: उन्होंने दम्तिण-पूर्व दिज्ञामें तुर्खखुको, पश्चिममें द्रह्मुको, दद्षिणमें यदुको और जततरमें अनुको माण्डलिकपदपर नियुक्त किया; तथा पूरुकों सम्पूर्ण भूमण्डलके राज्यपर सर्वपृथ्वीपति पूरे सोइभिषिच्य बन॑ ययौं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7495)
- **Original**: अभिषिक्तकर स्वयं वनकों चले गये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7496)
- **Original**: #णणण00 हर "न+- इति श्रीविष्णुपुराणे चतुर्थेडशे दशमो5ध्याय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7497)
- **Original**: _उप->न्‍न्‍कम्कक ैः अन+ ग्यारह॒वाँ अध्याय यदुवंशका वर्णन और सहस्रार्जुनका चरित्र श्रीपराज्षर उवाच अतः: पर॑ ययाते: ग्रथमपुत्रस्य यदोर्व॑शमहं कथयापि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7498)
- **Original**: यत्राइेषछोकनिवासो मनुष्य- सिद्धगन्धर्वयक्षराक्षसगुह्मकर्किंपुरुषाप्सरठरग- विहगदैत्यदानवादित्यरुद्भवस्वश्चिमरुद्देवर्षिभि- मुमुक्षुभिर्धर्मार्थकाममोक्षार्थिभिश्ष॒ तत्तत्फल- लाभाय सदाभिष्ठुतो5परिस्छेद्यमाहात्प्यांशेन भगवाननादिनिधनो.. विष्णुस्व॒ततार
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7499)
- **Original**: अत्र इलोक:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7500)
- **Original**: वदोर्वश॑नरः श्रुत्वा सर्वपापै: प्रमुच्यते
- **Translation**: 

---

