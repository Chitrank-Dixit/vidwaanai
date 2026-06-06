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

### Verse 1 (Vaivtpuran 22.18263)
- **Original**: इति ते कथितं वत्स सर्वसम्पत्करं॑ परम्‌ । सर्वैश्वर्यप्रदेय। नाम कवच परमाद्धुतम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.18264)
- **Original**: गुरुमभ्यर्च्य विधिवत्‌ कवर्च धारयेत्तु यः । कण्ठे वा दक्षिणे बराहौँ स सर्वविजयी भवेत्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.18265)
- **Original**: महालक्ष्मी्गृईह तस्य न जहाति कदाचन । तस्य छायेव सततं सा चव जन्मनि जन्मनि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.18266)
- **Original**: इृंदे_ कवचमज़ात्वा भजेल्लक्ष्मी॑ सुमन्दधी: । शतलक्षप्रजप्तोषपि न॒ मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.18267)
- **Original**: इति ज्रीब्रह्मवैंवर्ते इद्रं प्रति हरिणोप्रदिन्टं लक्ष्मीककर्च सम्पूर्णय्‌। (गणपतिखण्ड 22। 1-17) नारायण उवाच सर्वसम्पत्प्रसस्थास्थ कवचस्य॒ प्रजापति: । ऋषिश्छन्दश्न बृहती देवी पद्मालया स्वयम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.18268)
- **Original**: थर्मार्थकामम्रोक्षेप्‌ विनियोग: प्रकीर्तित: । पुण्यबीज॑ च॒ महतां कबर्च परमाद्भुतम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.18269)
- **Original**: 3» ही कमलवासिन्य॑ स्वाहा मे पातु मस्तकम्‌ । श्रीं मे पातु कपालं च लोचने श्रीं ख्रिये नमः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.18270)
- **Original**: 3» श्रीं श्रियै स्वाहेति चर कर्णयुग्मं सदावतु । 3 श्रीं हीं क्लीं महालक्ष्म्यै स्वाहा मे पातु नासिकाम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.18271)
- **Original**: 3» भ्रीं पद्मालयायै च स्वाहा दन्तं सदाबतु। 3» श्रीं कृष्णप्रियाय॑ च दन्तरन्ध॑ सदाबतु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.18789)
- **Original**: <रर2 * संक्षिप्त ब्रह्मवैवर्तपुराण « 200600902
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.18790)
- **Original**: 65089082/505808%/092%222262%258%6%8%55
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.18791)
- **Original**: 565%%252%%#55%2552%8%25096908 68 88 पषोडशारेण चक्रेण सुतीक्षणेनातितेजसा । जहि मां जगतां नाथ सद्धक्ति कुरु मोक्षद्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.18792)
- **Original**: त्वमंशेन वराहश्च॒ समुद्धर्तु वसुन्धराम्‌ । वेदानां... रक्षिता नाथ हिरण्याक्षनिषूदन:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.18793)
- **Original**: त्व॑ नृसिंह: स्वयं पूर्णों हिरण्यकशिपोर्वधे। प्रह्मादानुग्रहा्थाम_ देवानां रक्षणाय. च
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.18794)
- **Original**: त्व॑च्र॒ वेदोद्धारकर्ता मीनांशेन दयानिधे। नृपस्थ. ज्ञानदानाय रक्षाये सुरविप्रयो:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.18795)
- **Original**: शेषाधारश्ष कूर्मस्त्वपंशेष सृष्टिहेतवे । विश्वाधारश्ष॒ शेषस्त्वमंशेनापि. सहस््रदूक्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.18796)
- **Original**: रामो दाशरथिस्त्व॑ च जानक्युद्धारहेतवे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.18797)
- **Original**: दशकन्धरहन्ता च॑ सिन्धौ सेतुविधायक:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.18798)
- **Original**: कलया परशुरामश्च॒ जमदग्रिसुतो महान्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.18799)
- **Original**: त्रिःसप्तकृत्तो भूपानां निहन्ता जगतीपते
- **Translation**: 

---

