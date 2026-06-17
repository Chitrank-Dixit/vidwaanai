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

### Verse 1 (Nard Puran 0.561)
- **Original**: 142 संक्षिप्त नारदपुराण करता हूँ। जिनके रूपको, जिनके बल और
- **Translation**: 

---

### Verse 2 (Nard Puran 0.562)
- **Original**: हूँ, मोहसे व्याकुल हूँ, सैकड़ों कामनाओंने मुझे प्रभावको, जिनके लविविध कर्मोंकों तथा जिनके
- **Translation**: 

---

### Verse 3 (Nard Puran 0.563)
- **Original**: बाँध रखा है। मैं अकीर्तिभागी, चुगला, कृतघ्न, प्रमाणको ब्रह्मा आदि देवता भी नहीं जानते, उन
- **Translation**: 

---

### Verse 4 (Nard Puran 0.564)
- **Original**: सदा अपवित्र, पापपरायण तथा अत्यन्त क्रोधी हूँ। आत्मस्वरूप श्रीहरिकी स्तुति मैं कैसे कर सकता
- **Translation**: 

---

### Verse 5 (Nard Puran 0.565)
- **Original**: दयासागर! मुझ भयभीतकी रक्षा कौजिये। मैं हूँ? मैं संसार-समुद्रमें गिरा हुआ एक दीन मनुष्य
- **Translation**: 

---

### Verse 6 (Nard Puran 0.566)
- **Original**: बार-बार आपकी शरण लेता हूँ*। 1. ततो5स्मि नारायणमादिदेव॑ जगन्निवासं जगदेकबन्धुप्‌
- **Translation**: 

---

### Verse 7 (Nard Puran 0.567)
- **Original**: चक्राब्जशार्ड्रसिधरं महात्ते स्पृतातिनिष्ने शरणं प्रपद्चे
- **Translation**: 

---

### Verse 8 (Nard Puran 0.568)
- **Original**: यत्राभिजाब्जप्रभवों विधाता सृजत्यमुं लोकसमुच्चय॑ च
- **Translation**: 

---

### Verse 9 (Nard Puran 0.569)
- **Original**: यत्क्रोधजो हन्ति जगच्च रुद्रस्तमादिदेयं प्रणतो5स्मि विष्णुम्‌
- **Translation**: 

---

### Verse 10 (Nard Puran 0.570)
- **Original**: पद्मापतिं पद्मदलायताक्ष॑ विचित्रवीय॑निखिलैकहेतुम्‌ । वेदान्तवेच्य॑ पुरुष॑ पुराणं तेजोनिधिं विष्णुमहं प्रपन्न:
- **Translation**: 

---

### Verse 11 (Nard Puran 0.571)
- **Original**: आत्माक्षर सर्वगते5 च्युताज्यो ज्ञानात्मको ज्ञानविदां शरण्य: । ज्ञानैकवेद्यो भगवाननादि: प्रसीदतां व्यश्टिसमष्टिरूप:
- **Translation**: 

---

### Verse 12 (Nard Puran 0.572)
- **Original**: अनन्तवीयों गुणजातिहीनो गुणात्यको ज्ञानविरदां वरिष्ठ: । नित्य: प्रफन्नार्तिहर: परात्मा दयाम्बुधिमें बरदस्तु भूयात्‌
- **Translation**: 

---

### Verse 13 (Nard Puran 0.573)
- **Original**: यः स्थूलसूक्ष्मादिविशेषभेदैर्जगद्यथावत्स्वकृतं प्रविष्ट:
- **Translation**: 

---

### Verse 14 (Nard Puran 0.574)
- **Original**: त्वमेव तत्सर्वमनन्तसार: त्वत्त: परं नास्ति यत: परात्मनू
- **Translation**: 

---

### Verse 15 (Nard Puran 0.575)
- **Original**: अगोचरं यत्तव शुद्धरूपं मायाविहीनं गुणजातिहीनम्‌। निर्ञन॑ निर्मेलमप्रमेयं पश्यन्ति सन्त: परमार्थर्सक्ञम्‌
- **Translation**: 

---

### Verse 16 (Nard Puran 0.576)
- **Original**: एकेन हेग्नैव विभूषणानि यातानि भेदत्त्वमुपाधिभेदात्‌ । तथैव सर्वेश्वर एक एव प्रदृश्यते घिन्न इबाखिलात्मा
- **Translation**: 

---

### Verse 17 (Nard Puran 0.577)
- **Original**: यन्मायया मोहितचेतसस्त पश्यन्ति नात्यानमपि प्रस्िद्धम्‌। त एवं सायारहितास्तदेव पश्यन्ति सर्वात्मकमात्मरूपम्‌
- **Translation**: 

---

### Verse 18 (Nard Puran 0.578)
- **Original**: लिभुं ज्योतिरनौपम्यं विष्णुसंज्ज नमाम्यहम्‌। समस्तपेतदुद्धृत॑ं यतो गन्न प्रतिप्ठितम्‌
- **Translation**: 

---

### Verse 19 (Nard Puran 0.579)
- **Original**: यतश्नैतन्यमायात॑ यद्रूप॑ तस्य वे. नमः । अप्रमेयमनाधारमाधाराधेयरूपकम्‌ परमानन्दचिन्सात्र वासुदेव॑ नतो5स्म्यहम्‌
- **Translation**: 

---

### Verse 20 (Nard Puran 0.580)
- **Original**: हृदंगुहानिलय॑ देव॑ योगिभि: परिसेवितम्‌
- **Translation**: 

---

