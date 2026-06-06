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

### Verse 1 (Vaivtpuran 65.18847)
- **Original**: 824 « संक्षिप्त ख्रह्मवैवर्तपुराण « 5:2+349-%43-32.34+34.+%4-5593,339»+>+++++ 04-20... नवीनजलदश्याम॑ भीलेन्दीवरलोचनम्‌। पीतवस्व्रसमायुक्तकटिदेशविराजितम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 65.18848)
- **Original**: धूलिधूसरिताडूं च कि वा चन्दनचर्चितम्‌ । अथवा नवनीताक्तमड़ं. द्रक्ष्यमभि सस्मितम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 65.18849)
- **Original**: कि वा विनोदमुरलीं बरादयन्तं मनोहरम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 65.18850)
- **Original**: कि था गयां समूह च चारयन्तमितस्ततः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 65.18851)
- **Original**: किं बा वसन्‍्तं गच्छन्तं शयान॑ वा सुनिश्चितम्‌ । निदेश कीदृशं चाह्य सुदृष्ठा च शुभे क्षणे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 65.18852)
- **Original**: यत्पादपडं ध्यायन्ते ब्रह्मविष्णुशिवादयः ।न हि. जानाति यस्यान्तमनन्तोउनन्तविग्रह:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 65.18853)
- **Original**: यत्प्रभाव॑ न जानन्ति देवा: सन्तश्न संततम्‌ । यस्य स्तोत्रे जडीभूता भीता देवी सरस्वती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 65.18854)
- **Original**: दासी नियुक्ता यहास्ये महालक्ष्मीक्ष लक्षिता । गड़ा यस्यथ पदाम्भोजन्निःसुता सत्त्वरूपिणी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 65.18855)
- **Original**: जन्ममृत्युजराव्याधिहरा त्रिभुवनात्‌_ परा । दर्शनस्पर्शनाभ्यां च नृणां पातकनाशिनी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 65.18856)
- **Original**: ध्यायते यत्पदाम्भोज॑ दुर्गा दुर्गतिनाशिनी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 65.18857)
- **Original**: औैलोक्यजननी . देवी. मूलप्रकृतिरीश्वरी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 65.18858)
- **Original**: लोप्लां कृपेषु विश्वानि महाविष्णोश्न यस्य च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 65.18859)
- **Original**: असंख्यानि विचित्राणि स्थूलातू स्थूलतरस्थ च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 65.18860)
- **Original**: सच यद्‌ षोडशांशश्न यस्य सर्वेश्वरस्य चर । त॑ ड्र्॒टं यामि हे बन्धों मायामानुषरूपिणम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 65.18861)
- **Original**: सर्व॑सर्वान्तिरात्मानं॑ सर्वज्ञं प्रकृते: परम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 65.18862)
- **Original**: ब्रह्मज्योति:स्वरूप॑. च भक्तानुग्रहविग्रहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 65.18863)
- **Original**: निर्गुणं उ्व निरीह च॒ निरानन्द निराभश्रयम्‌ । परम परमानन्द सानन्द नन्दनन्दनमू
- **Translation**: 

---

### Verse 18 (Vaivtpuran 65.18864)
- **Original**: स्वेच्छामयं सर्वपरं सर्वबीज॑ सनातनम्‌ । वदन्ति योगिन: शश्वद्‌ ध्यायन्तेडहर्निशं शिशुम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 65.18865)
- **Original**: मन्वन्तसहस्र॑ च् निराहार: कुशोदरः । पड़े पाडास्तपस्तेपे पुरा पाछे तु यत्कृते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 65.18866)
- **Original**: पुनः कुरू तपस्यां चर तदा द्रक्ष्यसि मामिति । सकृच्छब्दं च शुश्राव न ददर्श तथापि तम्‌
- **Translation**: 

---

