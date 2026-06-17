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

### Verse 1 (Sama Ved 0.3921)
- **Original**: बात प्रगाथ (विषमा बृहती, समा सतोबृहती) 1492-1493, 1513-1514
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3922)
- **Original**: ऊर्ध्वा बृहती 1494-1496, 1506-1508 । अनुष्टुप्‌ 1503-1505 । उष्णिक्‌ 1509-1512 । बृहती 1515-1517
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3923)
- **Original**: इति चतुर्दशो5 ध्याय:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3924)
- **Original**: ए+-+ध्सलजन>े न कक फे9ऊ....---
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3925)
- **Original**: अथ पज्चदशो5 ध्याय:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3926)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3927)
- **Original**: 1535. कस्ते जामिर्जनानामग्ने को दाश्चध्वर: । को ह कस्मिन्नसि श्रित:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3928)
- **Original**: है अग्निदेव ! मनुष्यों में आपका बन्धु कौन है ? श्रेष्ठ दान से कौन आपका यजन करता है ? आपके स्वरूप को कौन जानता है ? आपका आश्रय स्थल कहाँ स्थित है ?
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3929)
- **Original**: 1536. त्वं जामिर्जनानामग्ने मित्रो असि प्रिय: । सखा सखिभ्य ईड्यू:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3930)
- **Original**: हे अग्निदेव ! आप मनुष्यों से भ्रातृ-भाव रखने वाले, स्तोताओं के लिए प्रिय मित्र के तुल्य हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3931)
- **Original**: 1537.यजा नो मित्रावरुणा यजा देवाँ ऋतं बृहत्‌ । अग्ने यक्षिस्व॑ दमम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3932)
- **Original**: है अग्निदेव ! आप हमारे निमित्त मित्र और वरुण देवों का यजन (पूजन) करें । देवताओं का यजन (पूजन) करें । यज्ञ को पूजा करें तथा यज्ञशाला में पूजायोग्य भाव से रहें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3933)
- **Original**: 1538. ईडेन्यो नमस्यस्तिरस्तमांसि दर्शतः। समग्निरिध्यते वृषा
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3934)
- **Original**: स्तुत्य, प्रणम्य, अः्धकारनाशक, दर्शनीय और शक्तिशाली है अग्निदेव ! आप आहुतियों द्वारा भली प्रकार प्रज्वलित किये जाते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3935)
- **Original**: 1539.वृषों अग्नि: समिध्यते5श्वो न देववाहन: । त॑ हविष्मन्त ईडते
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3936)
- **Original**: बलशाली अअश्व जैसे राजा के वाहन को खींच कर ले जाते हैं, उसीप्रकार अग्निदेव, देवताओं तक हाँवे पहुँचाते हैं । उत्तम प्रकार से प्रदीप्त हुए, ऐसे अग्निदेव यजमान कौ स्तुतियों को प्राप्त करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3937)
- **Original**: 1540.वृषणं त्वा बय॑ वृषन्वृषण: समिधीमहि। अग्ने दीद्यतं बृहत्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3938)
- **Original**: है बलवान्‌ अग्निदेव ! घृतादि की हवि प्रदान करने वाले हम, शक्तिशाली, तेजस्वी और महान्‌ आपको (अग्नि को) प्राप्त करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3939)
- **Original**: 15491.उत्ते बृहन्तो अर्चयः समिधानस्थ दीदिव: । अग्ने शुक्रास ईरते
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3940)
- **Original**: हे तेजस्वी अग्निदेव ! भली प्रकार प्रदीष्त, महानता को प्रेरित करने वाली शक्तिदायक आपकी लपें वृद्धि को प्राप्त करती हैं
- **Translation**: 

---

