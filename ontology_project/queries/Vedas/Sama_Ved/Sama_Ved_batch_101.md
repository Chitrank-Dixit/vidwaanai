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

### Verse 1 (Sama Ved 0.2001)
- **Original**: 773.पवते हर्यतो हरिरति हरांसिं रंह्मा। अभ्यर्ष स्तोतृभ्यो वीरवच्यश:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2002)
- **Original**: वोरसन्तान तथा यशप्राप्ति के इच्छुक साथकों के लिए यह हरिताभ प्रिय सोमरस, शुद्धरूप में ख्वित होता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2003)
- **Original**: 774.प्र सुन्वानायान्धसो मर्तो न वष्ट तद्च: । अप श्वानमराधसं हता मर न भूगव:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2004)
- **Original**: । शोधित होते समय सोम के शब्द-नाद को हीन कर्म को इच्छा वाले न सूर्ने । है साधकों ! अयोग्य कुत्तों (श्वान -वृत्ति वालो) को इस श्रेष्ठ कार्य से दूर रखो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2005)
- **Original**: इति षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2006)
- **Original**: ह। ऊं कक
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2007)
- **Original**: 2.8 सामवेद-संहिता ऋषि, देवता, छन्द-विवरण ऋषि- श्रुतकक्ष अथवा सुकक्ष आड्रिसस 713-715, 722-724 । वसिष्ठ मैत्रावरुणि 716-718, 734-736, 749-754
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2008)
- **Original**: मेधातिधि काण्व और प्रियमेध आड्रिस 719-721
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2009)
- **Original**: । इरिम्बिठि काण्व 725-727 । कुसीदी काण्व 728-730 । ब्रिशोक काण्व 731-733 । विश्वामित्र गाधिन 737-739। मधुच्छन्दा वैश्वामित्र 740-742 । शुनःशेप आजीगर्ति 743-745 । नारद काण्व 746-748 । अवत्सार काश्यप 755-757 । शुनःशेष आजीगर्ति (कृत्रिम देवरात वैश्वामित्र) 758 । मेध्यातिथि काण्व 75 9-760 । असित काश्यप अथवा देवल 761, 763 । अमहोयु आज्विरस 762 । त्रित आप्त्य 764-766 । सप्तर्षिगण 767-768 । श्यावाश्र आत्रेय 769-771
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2010)
- **Original**: अग्नि चाक्षुप 772, 773 । प्रजापति वैश्वामित्र अथवा वाच्य छछ7ढ। देवता- इन्द्र 7193-748 । अग्नि 749-750 । उषा 751-752 । अश्विनीकुमार 75 3-754 । पवमान सोम 755-774 । छन्‍्द- अनुष्टपू 713, 774 । गायत्री 714-745, 755-766, 769-771 । उष्णिक्‌ 746-748,772, 773 । बाहँत प्रगाथ (विषमा बृहती, समा सतोबृहती) 749-754, 767-768 ।
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2011)
- **Original**: इति द्वितीयो5 ध्याय:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2012)
- **Original**: जज आ 55 आप
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2013)
- **Original**: अथ तृतीयो5 ध्याय:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2014)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2015)
- **Original**: 775. पवस्व वाचो अग्रियः सोम चित्राभिरूतिभि: । अभि विश्वानि काव्या
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2016)
- **Original**: हे सोमदेव ! आप सर्वश्रेष्ठ हैं। अत: विभिन्न रक्षा साधनों से युक्त होकर हमारी हर प्रकार की स्तुतियों को सुनकर उनके शब्दों पर ध्यान दें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2017)
- **Original**: 776,.त्वं समुद्रिया अपो5ग्रियो बाच ईरयन्‌। पवस्व विश्वचर्षणे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2018)
- **Original**: हे सर्व हितकारी सोमदेव ! आप अग्रणी होकर हमरो स्तुतियों से प्रसन हुए, देवलोक के जल का आवाहन करें । यही पवित्र जल सोमरस में मिलाया जाता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2019)
- **Original**: 7757.तुभ्येमा भुवना कवे महिम्ने सोम तस्थिरे । तुध्यं धावन्ति धेनवः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2020)
- **Original**: हे दूरदर्शी सोमदेव ! आपकी महत्ता के प्रभाव से यह विश्व स्थित है । आपके लिए दूध उपलब्ध कराने हेतु, देबगणों को तृप्त करने वाली गौएँ आपके पास आ रहो हैं
- **Translation**: 

---

