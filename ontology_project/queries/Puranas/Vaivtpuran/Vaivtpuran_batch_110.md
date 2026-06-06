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

### Verse 1 (Vaivtpuran 7.18582)
- **Original**: नवीननीरदश्यामं॑ शोभित॑ पीतवाससा । चन्दनागुरुकस्तूरीकुडरुमद्रबचर्चितम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.18583)
- **Original**: शरत्पार्वणचन्द्रास्यं विम्बाधरमनोहरम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.18584)
- **Original**: मयूरपिच्छचूड़. च सद्रलमुकुटोस्म्वलम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.18585)
- **Original**: ब्रिभड्रलक्रमध्य॑ च बनमालाविभूषितम्‌ ।अ्रीवत्सवक्षस॑ चारुकौस्तुभेन विराजितम्‌। किशोरवयस शान्त॑ कान्‍्त॑ ब्रह्ेशयो: परम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.18586)
- **Original**: ददर्श वसुदेवक्ष देवकी पुरतो मुने। तुष्टाथ परया भकत्या विस्मयं परम॑ ययौ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.18587)
- **Original**: इति अब्रह्मवैवर्ते आविर्भधावकालिकअ्रीकृष्णस्वरूपवर्णनं सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 7। 72--78) हजडजलज#30%42509......000 देवक्‍्या सह वसुदेवेन कृतं अश्रीकृष्णस्तोत्रम्‌ बसुदेव उबाच श्रीमन्तमिन्द्रियातीतमक्षर॑. निर्गुणं विभुम्‌। ध्यानासाध्य॑ च॒ सर्वेषां परमात्मानमी श्वरम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.18588)
- **Original**: स्वेच्छामयं सर्वरूपं स्वेच्छारूपधरं परम्‌। निर्लिपं परम॑ ब्रह्म बीजरूपं॑ सनातनम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.18589)
- **Original**: स्थूलातू स्थूलतरं व्याप्तमतिसूक्ष्ममदर्शनम्‌ । स्थित सर्वशरीरेषु. साक्षिरूपमदृश्यकम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.18590)
- **Original**: शरीरवन्तं सगुणमशरीर॑ गुणोत्करम्‌ । प्रकृतिं प्रकृतीश च॒ प्राकृतं॑ प्रकृतेः परम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.18591)
- **Original**: सर्वेश सर्वरूप॑ च सर्वान्तकरमव्ययम्‌ । सर्वाधारं निराधारं निव्यूंह स्तौमि कि विभो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.18592)
- **Original**: अनन्तः स्तवने5शक्तो5शक्ता देवी सरस्वती। यं स्तोतुमसमर्थश्ष॒ पद्चवक्त्र: षडानन:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.18593)
- **Original**: चतुर्मुखो वेदकर्ता ये स्तोतुमक्षम: सदा । गणेशो न समर्थश्च॒योगीनद्राणां गुरो्गुरु:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.18594)
- **Original**: ऋषयो . देवताश्ैव मुनीझ्धमनुमानवा:। स्वप्रे तेघामदृश्यं च॒ त्वामेबं॑ कि स्तुबन्ति ते
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.18595)
- **Original**: श्रुतथ: स्तवनेउशक्ता: किं स्तुवन्ति विपश्चित:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.18596)
- **Original**: विहायैबव॑ शरीर॑ च बालो भवितुपतईसि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.18597)
- **Original**: वसुदेवकृतं॑ स्तोत्र तअिसंध्यं यः पठेन्नर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.18598)
- **Original**: भ्क्तिदास्यमवाप्रोति श्रीकृष्णचरणाम्बुजे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.18599)
- **Original**: विशिष्टपुत्र॑ लभते . हरिदासं गुणान्वितम्‌ । संकर्ट निस्तरेत्‌ तूर्ण शत्रुभीत्या: प्रमुच्यते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.18600)
- **Original**: इति श्रीब्रह्मवैवर्ते वस्ुदेवकृत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 7। 80--90 ) हजहअ कर क्‍5200000
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.464)
- **Original**: + स्रहास्वण्ड « रहे ऋकऋऋऋऋऊऋकऊऋऋऋकऋ ऋ$ऋ
- **Translation**: 

---

