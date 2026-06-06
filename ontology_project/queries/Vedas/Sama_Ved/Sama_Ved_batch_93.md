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

### Verse 1 (Sama Ved 0.1841)
- **Original**: इत्िि षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1842)
- **Original**: ऋषि, देवता, छन्द-विवरण ऋषि- असित काश्यप अथवा देवल 651-653
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1843)
- **Original**: कश्यप मारीच 654-656
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1844)
- **Original**: शत वैखानस 657-659 । भरद्वाज बार्हस्पत्य 660-662, 70 2-707 । विश्वामित्र गाधिन 663-664, 669-671
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1845)
- **Original**: विश्वामित्र गाधिन अधवा जमदग्नि 665 । इरिम्बिटि काण्य 666-668 । अमहीयु आड्रिरस 672-674 । सप्तर्षिगण 675-676 । उशना काव्य 677-679
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1846)
- **Original**: वसिष्ठ मैत्रावरुण 680-681 । वामदेव गौतम 682-684 । नोधा गोतम 685-686 । कलि प्रागाथ 687-688 । मधुच्छन्दा वैश्ञामित्र 689-691। गौरवीति शावत्य 692, 693 । अग्नि चाक्षुप 694-696 । अन्धीगु श्यावाश्वि 697- 699 । कवि भार्गव 700-702
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1847)
- **Original**: शंयु बार्हस्पत्य (तृणपाणि) 703-704
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1848)
- **Original**: सोभरि काण्व 708-709। नृमेध आइ्विरस 710-712
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1849)
- **Original**: देवता- पवमान सोम 651-659, 672-679, 672-679, 689-702
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1850)
- **Original**: अग्नि 660-662, 703-707 । मित्रावरुण 663-665 । इन्द्र 666-668, 680-688, 708-712 । इन्धाग्नी 669-671
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1851)
- **Original**: छन्‍्द- गायत्री 651-674, 682, 683, 689-691, 698, 699, 705-707 । बात प्रगाथ (विषमा बहती, समा सतोबृहती) 675-676, 680-681,685-688, 70 3-704 । त्रिप्रुप्‌ 677-679 । पादनिचृत्‌ गायत्री 684 । काकुभ प्रगाध (विषमा ककुफन्समा सतोबृहती) 69 2-693, 708-709 । उष्णिक्‌ 694-696, 716
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1852)
- **Original**: अनुष्टुप्‌ 6697 । जगती 700-702 । ककुप्‌ 710 । पुर उष्णिक्‌ 732 ।
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1853)
- **Original**: इति प्रथमो5 ध्याय:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1854)
- **Original**: ्ाछितजस- कम फिीआखण।ख
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1855)
- **Original**: द्वितीयो5 ध्याय:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1856)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1857)
- **Original**: 713.पान्तमा वो अन्धस इन्द्रमि प्र गायत । विश्वासाहं शतक्तु मंहिष्ठं चर्षणीनाम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1858)
- **Original**: है ऋत्विजो ! शत्रुनाशक, ऐश्वर्यदाता, शतक्रतु (सौ यज्ञ करने वाले) , आपके द्वारा उपलब्ध कराये गये अन्नरूप सोमरस का पान करने वाले इन्द्रदेव की प्रार्थना करो
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1859)
- **Original**: 714.पुरुहूतं पुरुष्टुत॑ गाथान्यां3 सनश्रुतम्‌ । इन्द्र इति ब्रवीतन
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1860)
- **Original**: सहायता के लिए बहुतों द्वारा बुलाये जाने वाले, अनेकों द्रारा जिनकी स्तुति को जातो है, हे कग्रत्विजो ! सनातन काल से प्रसिद्ध, उन इन्द्रदेव की वन्दना करो
- **Translation**: 

---

