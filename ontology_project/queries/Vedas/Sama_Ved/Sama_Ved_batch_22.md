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

### Verse 1 (Sama Ved 0.421)
- **Original**: [पिछले
- **Translation**: 

---

### Verse 2 (Sama Ved 0.422)
- **Original**: में किये गये प्रश्न का उत्तर यहाँ दिया गया है ।] ( परमात्मा) पर्वत की घाटियों (शान्त स्थानों) एवं नदियों के संगम, पवित्र स्थलों पर श्रद्धापूर्वक ध्यान के द्वारा सत्पुरुष (परमात्मा की) आराधना करते हैं और वहीं उन्हें (इन को) प्राप्त करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.423)
- **Original**: 944. प्र संप्राजं चर्षणीनामिन्द्रं स्तोता नव्यं गीर्भि: । नर॑ नृषाहं मंहिष्ठम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.424)
- **Original**: मनुष्यों में भलीप्रकार प्रतिष्ठा प्राप्त, स्तुति किये जाने योग्य, शत्रुजयी नेता, उन महान्‌ इन्द्रदेव की स्तुति करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.425)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.426)
- **Original**: के जे फ
- **Translation**: 

---

### Verse 7 (Sama Ved 0.427)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.428)
- **Original**: 145. अपादु शिफ्रद्यन्धसः सुदक्षस्य प्रहोषिण: । इन्दोरिन्द्रो यवाशिर:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.429)
- **Original**: मुकुट धारी इन्द्रदेव ने, देवताओं के लिए हृवि देने में निपुण याज्जिकों के जौ के आटे और दूध से मिश्रित सोमरस रूपी हविष्यान्न को ग्रहण किया
- **Translation**: 

---

### Verse 10 (Sama Ved 0.430)
- **Original**: 146. इमा उ त्वा पुरूवसोभि प्र नोनुवुर्गिर: । गावो वत्सं न धेनव:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.431)
- **Original**: हे ऐश्वर्यवान्‌ इन्द्रदेव ! दूध देने वाली गौएँ जिस प्रकार अपने बछड़ों के पास जाने के लिए लालायित रहती हैं । उसी लालसा से हम आपके निमित्त स्तवन करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.432)
- **Original**: 147. अत्राह गोरमन्वत नाम त्वष्टुरपीच्यम्‌ । इत्था चन्द्रमसो गृहे
- **Translation**: 

---

### Verse 13 (Sama Ved 0.433)
- **Original**: मनोषियों की मान्यता के अनुसार रात्रि में सूर्य के छिप जाने पर भी संसार को तुष्ट करने वाले सूर्यदेव का दिव्य तेज, गतिमान्‌ चन्द्रमण्डल में दृष्टिगोचर होता है.
- **Translation**: 

---

### Verse 14 (Sama Ved 0.434)
- **Original**: 148. यदिन्द्रो अनयद्वितो महीरपो वृषन्तम: । तत्र पृषाभुवत्सचा
- **Translation**: 

---

### Verse 15 (Sama Ved 0.435)
- **Original**: जब महाबली इन्द्रदेव, घनघोर जल वृष्टि के रूप में जल को प्रवाहित करते हैं, तब पोषण करने में समर्थ (पूषा) भी उनके सहयोगी होते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.436)
- **Original**: [ वर्षा के जल में पोषक तत्व संयुक्त हो जाते हैं ।] 149. गौर्धयति मसरुतां श्रवस्युर्माता मघोनाम्‌। युक्‍ता वह्ली रधानाम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.437)
- **Original**: धन-सम्पन्न, मरुतों के साथ अग्निरथ के माध्यम से जुड़ी हुई. अन्नादि उत्पन्न करने की इच्छा रखने वाली पृथ्वी माता दूध (सोम) पान करती हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.438)
- **Original**: 150. उप नो हरिभिः सुतं याहि मदानां पते । उप नो हरिभि: सुतम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.439)
- **Original**: है सोमाधिपति इन्द्रदेव ! अपने श्रेष्ठ घोड़ों के द्वारा हमारे सोमयज्ञ में आप बार-बार पथारें
- **Translation**: 

---

### Verse 20 (Sama Ved 0.440)
- **Original**: 159, इृष्टा होत्रा असक्षतेन्द्रं वृधन्तो अध्चरे। अच्छावभूथमोजसा
- **Translation**: 

---

