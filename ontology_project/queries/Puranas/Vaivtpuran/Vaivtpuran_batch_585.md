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

### Verse 1 (Vaivtpuran 45.4561)
- **Original**: वैसी वस्तुकों सौगुनी संख्यामें पा जाते हैं। मुने! तुम मेरी दयारूपिणी भगिनी और माताके समान
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4562)
- **Original**: इस प्रकार इन्द्र देवी मनसाकी स्तुति करके वस्त्र क्षमाशील हो। सुरेश्वरि! तुमने पुत्र और स्त्रीसहित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4563)
- **Original**: और आभूषणोंसे विभूषित उस बहिनको साथ ले मेरे प्राणोंकी रक्षा की है, मैं तुम्हें पूजनीया बनाता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4564)
- **Original**: अपने निवास-स्थानकों चले गये।* देवि त्वां स्तोतुमिच्छामि साध्वीनां प्रवरां वराम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4565)
- **Original**: परात्पां च परमां न हि स्तोतु क्षमो5धुना। स्तोत्राणां लक्षणं वेदे स्वभावाख्यानतत्परम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4566)
- **Original**: न क्षमः प्रकृते यक्तुं गुणानां तव सुव्ते। शुद्धसत््वस्वरूपा त्व॑ कोपहिंसाविवर्जिता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4567)
- **Original**: न च शप्तो मुनिस्तेन त्यक्तया च त्वया यतः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4568)
- **Original**: त्वं मया पूजिता साध्वि जननी मे यथादिति:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4569)
- **Original**: दयारूपा च भगिनी क्षमारूपा यथा प्रसू:। त्वया में रक्षिता: प्राणा: पुत्रदारा: सुरेश्वारि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.17941)
- **Original**: 792 + संक्षिप्त ्रह्मवैवर्तपुराण * #%&#######%$%###$#%$%$%$%#$#%#%###%$$%$%#%$#%#$%$$%$%%ऊऋऊऋ$%%ऊऋऋ$ऊऋ$%ऊऋ$%ऊ$%ऋ%ऊऋऋ%$%%%ऊक%ऊ%$%%#$%%#####% #%# चतन्धमा बलवांस्तुष्टो येषां भाग्यवतां भूगों
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.17942)
- **Original**: तेषां तारागणा रुष्टाः कि कुर्वन्ति च दुर्बला:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.17943)
- **Original**: यस्य तुष्ट: सभायां चेन्नरदेवों महान्‌ सुखी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.17944)
- **Original**: तस्य कि वा करिष्यन्ति रुष्टा भृत्याश्न दुर्बला:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.17945)
- **Original**: इत्युक्त्वा पार्वती तुष्टा दत्त्वा राम॑ शुभाशिषम्‌ । जगामान्तः:पुरं॑ तूर्ण हरिशब्दो बभूव हु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.17946)
- **Original**: स्तोत्र वै काण्वशाखोक्त पूजाकाले च थ: पठेत्‌ । बात्राकाले च॒ प्रातर्वा वाज्छितार्थ लभेद्‌ श्रुवम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.17947)
- **Original**: पत्रार्थी लभते पुत्र॑ कन्यार्थी कन्यकां लभेत्‌ । विद्यार्थी लभते विद्यां प्रजार्थी चाप्तुयात्‌ प्रजाम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.17948)
- **Original**: भ्रष्टराज्यों लभेद्‌ राज्यं नष्टवित्तो धनं लभेतू
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.17949)
- **Original**: यस्य सरुष्टो गुरुर्देवों राजा वा बान्धवोईथवा । तस्य तुष्ठश्ध बरदः स्तोत्रराजप्रसादतः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.17950)
- **Original**: दस्युग्रस्तो5हिग्रस्तश्च॒ शत्रुग्रस्तो भयानकः । व्याधिग्रस्तो भवेन्मुक्त: स्तोत्रस्मरणमात्रतः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.17951)
- **Original**: राजद्वारे श्मशाने च कारागारें च बन्धने । जलराशौ.. निमग्रश्न॒ मुक्तस्तत्स्मृतिमात्रत:
- **Translation**: 

---

