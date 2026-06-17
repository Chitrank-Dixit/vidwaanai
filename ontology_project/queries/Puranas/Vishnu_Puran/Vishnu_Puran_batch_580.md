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

### Verse 1 (Vishnu Puran 0.11581)
- **Original**: तदनन्तर कौरबोने बलरामजीके सहित साम्बका पूजन किया तथा बहुत-से दहेज और वधूके सहित उन्हें द्वास्कापुरी भेज दिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11582)
- **Original**: जा इति श्रीविष्णूप्राणे पञ्ममेंडशे पञ्जत्रिशोंउध्यायः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11583)
- **Original**: 408 रख छछज अओ्रीविष्पुराण छ उऊछइछ छः £आःरेश अश्रीविष्णुपुराण ( आ* 36 छत्तीसवाँ अध्याय ड्विखिद-वध श्रीपराज्र उवाच श्रीपरावारजी बोले--हे मैत्रेय ! बलद्ाली देवपक्षविरोधिनः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11584)
- **Original**: सखाभवन्‍्पहावीयों ट्विविदों वानर्भ:ः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11585)
- **Original**: 2 वैरानुबन्धे बलवान्स चकार सुराज्प्रति। नरके हतवान्कृष्णो देवराजेन चोदितः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11586)
- **Original**: 3 करिष्ये सर्वदेवानां तस्मादेतत्मतिक्रियाम्‌। यज्विध्वंसनं कुर्वन्‌ मर्त्यल्त्रेकक्षय तथा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11587)
- **Original**: 4 ततो विध्बंसयामास बज्ञानज्ञानमोहितः । बिभेद साधुमर्यादां क्षयं चक्रे च देहिनाम्‌ू
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11588)
- **Original**: 5 ददाह सबनान्देशान्पुरय्रामान्तराणि च। क्रचिश्च॒ पर्वताक्षेपैग्रामादीन्समचूर्णयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11589)
- **Original**: 6 औल्लनुत्पाट्य तोयेषु मुमोचाम्बुनिधो तथा । पुनश्चार्णवम्ध्यस्थ: क्षोभयामास सागरम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11590)
- **Original**: 7 तेन विक्षोभितश्चान्धिरुद्धेलो द्विज जायते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11591)
- **Original**: प्रावयंस्तीरजान्यामान्पुरादीनतिवेगवानू_
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11592)
- **Original**: 8 कापरूपी महारूप॑ कृत्वा सस्यान्यशेषतः । लुठन्भ्रमणसम्मर्दैस्सझूर्णयति. बानर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11593)
- **Original**: 9 तेन विप्रकृतें सर्व जगदेतहुरात्मना । निस्स्वाध्यायवषदकारं मैत्रेयासीत्सुदु:खितम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11594)
- **Original**: 10 रेबती च महाभागा तथैवान्या वरस्त्रिय:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11595)
- **Original**: 11 उद़बीयमानो विलसल्ललनामौलिमध्यग:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11596)
- **Original**: रेमे यदुकुलश्रेष्ठ; कुबेर इव मन्दरे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11597)
- **Original**: 12 ततस्स वानरो5ध्येत्य गृहीत्वा सीरिणो हलम्‌ । मुसलं च चकारास्य सम्मुखं च विडम्बनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11598)
- **Original**: 13 पानपूर्णाश्ष॒ करकाझिक्षेपाहत्य बै तदा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11599)
- **Original**: 14 बलरामजीका ऐसा ही पराक्रम था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11600)
- **Original**: अब, उत्होंने जो और एक़ कर्म क्रिया था वह भी सुनो
- **Translation**: 

---

