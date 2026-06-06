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

### Verse 1 (Sama Ved 0.3421)
- **Original**: 1337. अर्पा नः सोम शं गवे धुक्षस्व पिप्युषीमिषम्‌ । वर्धा समुद्रमुक्थ्य
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3422)
- **Original**: स्तुति करने योग्य हे सोम ! हमारी गौओं को सुख प्रदान करने वाले, हमारे घर को पौष्टिक अन्न से भरने वाले आप जल से मिश्रित होकर सुपात्र में स्थिर हों .
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3423)
- **Original**: इति एकादश: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3424)
- **Original**: द्वादश: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3425)
- **Original**: 1338. आघा ये अप्निमिन्धते स्तृणन्ति बर्हिरानुषक्‌ । येषामिन्द्रो युवा सखा
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3426)
- **Original**: अम्नि को प्रदीप्त करने वाले साधकों के, युवा इन्द्रदेव सदा हो मित्र रहते हैं । वे साधक देवों के लिए क्रमशः कुशाएँ (आसन) बिछाते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3427)
- **Original**: 1339. बृहन्निदिध्म एषां भूरि शस्त्र पृथु: स्वर: । येषामिन्द्रो युवा सखा
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3428)
- **Original**: ऋषियों के पास समिधाएँ पर्याप्त हैं। शख्त्र ( प्रार्थनाएँ) महान्‌ हैं। स्तोत्र भी असंख्य हैं । युवा इन्द्रदेव इनके सदा हो मित्र रहते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3429)
- **Original**: 1340. अयुद्ध इद्युधा वृतं शूर आजति सत्वभि: । येषामिन्द्रो युवा सखा
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3430)
- **Original**: इन्द्रदेव जिनके मित्र हैं, वह साधक युद्ध की इच्छा न रखते हुए भी सैन्यबल से युक्त शत्रु को पराजित करने में समर्थ होता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3431)
- **Original**: 1341. य एक इद्विदयते वसु मर्ताय दाशुषे । ईशानो अप्रतिष्कुत इन्द्रो अड़
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3432)
- **Original**: विश्व के स्वामी, युद्ध में अकेले होते हुए भी शत्रु से कभी पराजित न होने वाले इन्द्रदेव, याजकों को सम्पूर्ण वैभव प्रदान करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3433)
- **Original**: 1342.यश्चिद्धि त्वा बहुभ्य आ सुतावाँ आविवासति । उं्र॑ तत्पत्यते शव इन्द्रो अड़
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3434)
- **Original**: असंख्यों में से जो यजमान सोमयज्ञ करके आपकी आराधना करता है, उसे हे इन्द्रदेव ! आप अति शीघ्र बल सम्पन्न बना देते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3435)
- **Original**: 1343. कदा मर्तमराधसं पदा क्षुम्पमिव स्फुरत्‌ । कदा नः शुश्रवह्ििर इन्रों अड्र
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3436)
- **Original**: वे इन्द्रदेव हमारी स्तुतियों को कब सुनेंगे और आराधना न करने वालों को क्षुद्र पौधे की भाँति कब नष्ट करेंगे ?
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3437)
- **Original**: 1344. गायन्ति त्वा गायत्रिणोर्चत्यर्कमर्किण: । ब्रह्माणस्त्वा शतक्रत उद्दंशमिव येमिरे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3438)
- **Original**: हे शतकर्मा इन्द्रदेव ! स्तोतागण आपका गुण गान करते और मंत्रों द्वारा यजन करते हैं । बाँस की वृद्धि की भाँति ऋर्त्विग्गण महिमा गान द्वारा आपको उच्च पद प्रदान करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3439)
- **Original**: 10.12 सामवेद- संहिता 1345.यत्सानो: सान्वारुहो भूर्यस्पष्टे कर्त्वम्‌ । तदिन्द्रो अर्थ चेतति यूथेन वृष्णिरेजति
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3440)
- **Original**: जब यजमान समिधादि के निमित्त पर्वत पर जाते हैं और यजनकर्म करते हैं, तब उनके मनोरथ को जानने वाले इन्रदेव, इष्ट प्रदायक यज्ञ में जाने को उद्यत होते हैं
- **Translation**: 

---

