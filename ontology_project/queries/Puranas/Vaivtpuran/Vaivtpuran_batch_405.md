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

### Verse 1 (Vaivtpuran 21.18419)
- **Original**: करोति सृष्टि स॒विधेर्विधाता विधाय नित्यां प्रकृति जगत्प्रसूम्‌। ख्रद्मादय: प्राकृतिकाश्ष॒ सर्वे भक्तिप्रदां श्री प्रकृति भजन्ति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.18420)
- **Original**: ब्रह्मस्वरूपा प्रकृति्णन भिन्ना यया च सृष्टि कुरुते सनातनः। भ्रियश्च सर्वा: कलया जगत्सु माया तर सर्वे च्र तया विमोहिता:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.18421)
- **Original**: नारायणी सा परमा सनातनी शक्तिश्चन॒ पुंस: . परमात्मनश्। आत्मेश्श्नापि यया चत्॒ शक्तिमांस्या बिना स्पष्टमशक्त एब
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.18422)
- **Original**: इति औब्रह्मवैवर्ते श्रीगारायणर्षिकतों भगवत्स्तवः सम्पूर्ण: । (ब्रह्मखण्ड 30
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.18423)
- **Original**: 17-12) “30 ्येडथेएथ00 5,000
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.18424)
- **Original**: <10 + संक्षिप्त भ्रह्मवैयर्तपुराण « देवै: पार्वत्या च कृतं श्रीकृष्णस्तोत्रम्‌ एतस्मिन्नन्ते._ देवा: पार्वतीसहितास्तदा । सद्यो ददृशुराकाशे तेजसां निकरें परम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.18425)
- **Original**: कोटिसूर्यप्रभोध्व॑च्र॒प्रच्वलन्तं दिशों दश
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.18426)
- **Original**: कैलासशैलं॑ पुरतः.. सर्वदेवादिभिर्युतम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.18427)
- **Original**: स्वान्‌ कुर्वन्तं प्रच्छन्न॑ विस्तीर्णमण्डलाकृतिम्‌ । दृष्ठा त॑ च भगवतस्तुष्टवुस्ते क्रमेण च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.18428)
- **Original**: विष्णुरुवाच ब्रह्माण्डानि च सर्वाणि यलल्‍्लोमविवरेघषु स॑ । सोउर्य ते घोडशांशश्च के बय॑ यो महाविराद्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.18429)
- **Original**: ब्रह्मोचाच वेदोपयुक्त दृश्य॑ यत्‌ प्रत्यक्ष॑ द्रष्टमीश्वर । स्तोतुं तद्‌ बर्णितुमह शक्त: किं स्तौमि तत्परम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.18430)
- **Original**: श्रीमहादेव उवाच ज्ञनाधिष्ठातृदेवो5हं स्तौमि ज्ञानपरं च किम्‌ । सर्वानिर्वचनीयं य॑ त॑ त्वां स्वेच्छामय विभुम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.18431)
- **Original**: धर्म उवाच अदृश्यमवबतारेषु यद्‌ दृश्यं सर्वजन्तुभि: । कि स्तौमि तेजोरूपं तद्‌ भक्तानुग्रहविग्रहम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.18432)
- **Original**: देवा ऊचु: के बय॑ त्वत्कलांशाश्न किं वा त्वां स्तोतुमीश्वरा: । स्तोतुं न शक्ता बेदा य॑ न चर शक्ता सरस्वती
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.18433)
- **Original**: मुनय ऊचु: वेदान्‌ पठित्वा विद्वांसो वयं कि वेदकारणम्‌ । स्तोतुमीशा न वाणी च त्वां च वाइमनसो: परम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.18434)
- **Original**: सरस्वत्युवाच बागथिष्ठातृदेवी मां बदन्ति वेदबादिन: । किद्ञिन्न शक्ता त्वां स्तोतुमहों बाइमनसो: परम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.18435)
- **Original**: सावितन्र्युवाच वेदप्रसूरहू॑ नाथ सृष्टा त्वत्कलया पुरा । किं स्तौमि स्त्रीस्वभावेन सर्वकारणकारणम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.18436)
- **Original**: लक्ष्मीरुवाच त्वदंशविष्णुकान्ताईं जगत्पोषणकारिणी । किं स्तौमि त्वत्कलासृष्टा जगतां बीजकारणम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.18437)
- **Original**: हिमालय उबाच हसन्ति सन्‍्तो मां नाथ कर्मणा स्थावर॑ परम्‌ । स्तोतुं समुद्यतं क्षुद्रः कि स्तौमि स्तोतुमक्षम:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.18438)
- **Original**: क्रमेण सर्वे त॑ स्तुत्वा देवा विररमुर्मुने
- **Translation**: 

---

