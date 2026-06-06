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

### Verse 1 (Rig Ved 0.701)
- **Original**: 314 यत्र द्वाविव जघनाधिषवण्या कृता। उलूखलसुतानामवेद्विन्दर जल्गुल:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.702)
- **Original**: हे इद्धदेव ! जहाँ दो जंघाओं के समान विस्तृत, सोम कूटने के दो फलक रखे हैं, वहाँ ( यज्ञशाला में) उलूखल से निष्पनन सोम का पान करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.703)
- **Original**: 315 यत्र नार्यपच्यवमुपच्यवं च शिक्षते । उलूखलसुतानामवेद्विन्द्र जल्गुल:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.704)
- **Original**: हे इद्धदेव ! जहाँ गृहिणी सोमरस तैयार करने के लिए कूटने (मूसल चलाने) का अभ्यास करती है, वहाँ ( यज्ञशाला में ) उलूखल से निष्पन सोमरस का पान करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.705)
- **Original**: के ऋग्वेद संहिता भाग-1 316. यत्र मन्धां विबध्नते रश्मीन्यमितवा इब। उलूखलसुतानामवेद्विद्ध जल्गुल:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.706)
- **Original**: हे इन्द्रदेव ! जहाँ सारथी द्वारा घोड़े को लगाम लगाने के समान (मधानी को) रस्सी से बॉधकर मन्थन करते है, वहाँ ( यज्ञशाला में ) उलुखल से निष्पन हुए सोमरसत का पान करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.707)
- **Original**: 317. यच्चिद्धि त्यं गृहेगृह उलूखलक युज्यसे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.708)
- **Original**: इह द्युमत्तमं वद जयतामिव दुन्दुभि:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.709)
- **Original**: है उलूखल ! यद्चपि घर-घर में तुमसे काम लिया जाता है, फिर भी हमारे घर में विजय-दुन्दुभि के समान उच्च शब्द करो
- **Translation**: 

---

### Verse 10 (Rig Ved 0.710)
- **Original**: 318. उत सम ते वनस्पते बातो वि वात्यग्रमित्‌। अथो इन्द्राय पातवे सुनु सोममुलूखल।
- **Translation**: 

---

### Verse 11 (Rig Ved 0.711)
- **Original**: हे उलूखल- मूसल रूप वनस्पते ! तुम्हारे सामने वायु विशेष गति से बहती है । हे उलुखल ! अब इन्द्देव के सेवनार्थ सोमरस का निष्पादन करो
- **Translation**: 

---

### Verse 12 (Rig Ved 0.712)
- **Original**: 319. आयजी वाजसातमा ता ह्यु1च्चा विजर्भुत:। हरी ड्वान्धांसि बप्सता
- **Translation**: 

---

### Verse 13 (Rig Ved 0.713)
- **Original**: यज्ञ के साथन रूप पूजन-योग्य वे उलूखल और मूसल दोनों, अन (चने) खाते हुए इन्धदेव के दोनों अश्वों के समान उच्च स्वर से शब्द करते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.714)
- **Original**: 320. ता नो अद्य बनस्पती ऋष्वावृष्वेभि: सोतृभि:। इन्द्राय मधुमत्सुतम्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.715)
- **Original**: दर्शनीय उलूखल एवं मूसल रूप हे वनस्पते ! आप दोनों सोमयाग करने वालों के साथ इ्धदेव के लिए मथुर सोमरस का निष्पादन करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.716)
- **Original**: 321. उच्छिष्टं चम्वोर्भर सोम॑ पवित्र आ सृज। नि थेहि गोरधि त्वचि
- **Translation**: 

---

### Verse 17 (Rig Ved 0.717)
- **Original**: उलूखल और मूसल द्वाग निष्पादित सोम को पात्र से निकालकर प्रवित्र कुशा के आसन पर रखें और अवशिष्ट को छानने के लिए पवित्र चर्म पर रखें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.718)
- **Original**: [ सूक्त - 29 ] [ऋषि-शुन: शेप आजीगर्ति (कृत्रिम देवरात वैश्वामित्र )
- **Translation**: 

---

### Verse 19 (Rig Ved 0.719)
- **Original**: देवता-इन्द्र
- **Translation**: 

---

### Verse 20 (Rig Ved 0.720)
- **Original**: छतद-पंक्ति ।] 322. यच्चिद्धि सत्य सोमपा अनाशस्ता इब स्मसि। आतू न इन्द्र शंसय गोष्वश्रेषु शुभ्रिषु सहस्नेषु तुवीमघ
- **Translation**: 

---

