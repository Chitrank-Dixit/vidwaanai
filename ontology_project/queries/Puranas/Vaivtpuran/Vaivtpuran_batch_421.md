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

### Verse 1 (Vaivtpuran 22.18800)
- **Original**: अंशेन कपिलस्त्य॑ च सिद्धानां च गुरोगुरु: । मातृज्ञापप्रयाता च . योगशास्त्रविधायक:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.18801)
- **Original**: अंशेन ज्ञानिनां श्रेष्ठी नरनारायणावृषी । त्व॑ चर धर्मसुतो भूत्वा लोकविस्तारकारक:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.18802)
- **Original**: अथुना कृष्णरूपस्त्य॑ परिपूर्णतम: स्वयम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.18803)
- **Original**: सर्वेषामवतारणां ब्रीजरूप: सनातन:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.18804)
- **Original**: यशोदाजीवनो.नित्यो नन्‍्दैकानन्दवर्धन: । प्राणाधिदेवों गोपीनां राश्राप्राणाश्रिक: प्रिय:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.18805)
- **Original**: बसुदेबसुतः शान्तो देवकीदुःखभज्जन: । अयोनिसम्भव: श्रीमानू_ पृथिवीभारहारकः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.18806)
- **Original**: पूतनाय॑ मातृगतिप्रदाता च॑ कृपानिधि: । बककेशिप्रलम्बानां. ममापि मोक्षकारक:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.18807)
- **Original**: स्वेच्छामय गुणातीत भक्तानां भयभझ्जन । प्रसीद राधिकानाथ प्रसीद कुरू मोक्षणम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.18808)
- **Original**: है नाथ गार्दभीयोने: समुद्धर भवार्णवात्‌ । मूर्ख॑स्त्वद्धक्तपुत्रोडहह मामुद्धतुँ._ त्वम्ईसि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.18809)
- **Original**: वेदा ब्रह्मादयों यं चर मुनीन्द्रा: स्तोतुमक्षमा: । किं स्तौमि त॑ गुणातीतं पुरा दैत्यो3धुना खरः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.18810)
- **Original**: एवं कुरु कृपासिन्थो येन मे न भवेज्जनुः । दृष्ठा पादारविन्द ते कः पुनर्भवनं ब्रजेत्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.18811)
- **Original**: ब्रह्मा स्तोता खरः स्तोता नोपहासितु्महसि । सदीश्चवरस्थ विज्ञस्थ योग्यायोग्ये समा कृपा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.18812)
- **Original**: इत्येबमुक्त्या दैत्येन्द्रस्तस्थी च॑ पुरतो हरे: । प्रसन्ननददन: श्रीमानतितुष्टोी. बभूबष ह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.18813)
- **Original**: इद दैत्यकृतं स्तोत्र नित्यं भक्‍त्या च यः पठेत्‌ । सालोक्यसाहिसामीप्य॑ लीलया लभते हरे:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.18814)
- **Original**: डृह लोके हरेर्भक्तिमन्ये दास्यं सुदुर्लभम्‌ । विद्यां श्रियं सुकवितां पुत्रपौत्रान्‌ू यशों लभेत्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.18815)
- **Original**: इति श्रीब्रह्मवैवर्ते दानवकृर्त श्रीकृष्णस्तोत्रं सस्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 22। 35--60 ) राधाकृतं श्रीकृष्णस्तोत्रम्‌ गराधिकोवाच गोलोकनाथ गोपीश मदीश प्राणबल्लभ । हे दीनबन्धो दीनेश सर्वेश्वर नमोस्तु ते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.18816)
- **Original**: गोपेश . गोसमूहेश. यशोदानन्दवर्धन । नन्दात्मज सदानन्द नित्यानन्द नमोस्तु ते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.18817)
- **Original**: शतमन्योर्मन्युभग्र ब्रह्मदर्घिवताशक । कालीयदमन प्राणदाथ कृष्ण नमोउस्तु ते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.18818)
- **Original**: शिवानन्तेश ब्रहदेश ब्राह्मणेश परात्पर । ब्रह्मस्वरूप द्वहाज्ञ ब्रह्मब्मीज नमोउस्तु ते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.18819)
- **Original**: चराचरतरोबीज _गुणातीत_गुणात्मक । गुणबीज गुणाधार गुणेश्वर नमोउस्तु ते
- **Translation**: 

---

