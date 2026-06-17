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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.61)
- **Original**: इस मंत्र से गौरी का आवाहन करके "ऊँ गौर्ये नम” कहकर यन्धाक्षतादि से विधिवत्‌ पूजन करे। यथा-- कुंकुम॑ कामदं दिव्य कामना-काम-सर्भवमू । कुंकुमेनार्चिते देवि ! प्रसत्ना भव सर्वदा
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.62)
- **Original**: हरिद्रानिर्षित॑ देवि ! सौभाग्यसुखसम्पदामू । अतस्त्वां पूजयिष्यामि यूहाण परमेश्वरि !
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.63)
- **Original**: अबीरं च गुलालं च चोवा चन्दनमेव च। अबीरेणार्चिता देवि ! अतः शान्ति प्रयच्छ में
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.64)
- **Original**: सिन्दूरं शोभनं रक्त सौभाग्य प्रियवर्द्धनमू । सुखदं मो क्षदं चैव सिन्दूरें प्रतिगृह्तामू !
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.65)
- **Original**: अक्षताश्च सुरश्नेष्ठे ! कुंकुमाक्ताः सुशोभिता: । मया निवेदिता भक्त्या यूहाण परमेश्वरि !
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.66)
- **Original**: माल्यादीनि सुगन्धीनि मालत्यादीनि सौख्यदे । मयाउ5्हतानि पूजार्थ पुष्पाणि प्रतिगृहतामु
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.67)
- **Original**: वनस्पतिरसोत्पन्नः सुगन्धाब्यों मनोहर: । आध्लेयः सर्वदेवानां धूपोघ्यं प्रतिगृह्मताम्‌
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.68)
- **Original**: साज्यज्ञ॒वर्तिसंयुक्ते वद्दिना योजित॑ मया। दीप॑ गृहाण देवेशि ! त्रैलोक्यतिमिरापहम्‌
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.69)
- **Original**: शर्कराखण्डखादयानि ... दधिक्षीर॒पृतानि च । आहार भक्ष्य-मोज्यज्न नैवेचं प्रतिगृह्मतामू
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.70)
- **Original**: [72 श्री विश्वकर्मा पुराण एक्पूजन पदति श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.71)
- **Original**: गंगाजल समानीतं. सुवर्णकलशो दूधृतम्‌ । आचम्यज्वैव देवेशि ! प्रीत्यर्थ प्रतियृह्नतामु
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.72)
- **Original**: इद॑ फलें मया देवि ! स्थापित पुरतस्तव । तेन से सफलावाप्ति्भवित्‌ जन्मनि-जन्मनि
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.73)
- **Original**: हिरण्यगर्भ-गर्भस्थ हेमबीजं . विभावसोः । अनन्तपुण्यफलदमतः शान्ति प्रयच्छ मे
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.74)
- **Original**: इसके बाद पुप्पाव्जलि देकर प्रार्थना करनी चाहिएँ। तदन्तर नवग्रह पूजन तथा षोडशमातृका-पूजन करे । नवग्रह पूजन मन्त्र ब्रह्मा मुरारिस्त्रपुरान्तकारी भानुः शशी भूमिसुत्तो बुघश्च । गुरुइच शुक्र: शनिराहुकेतवः सर्वे ग्रहाः शान्तिकरा भवन्तु
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.75)
- **Original**: 'नवसह्ठ चद्क उपर्युक्त मंत्रों से 'सूर्यादि बुँ
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.76)
- **Original**: च्यन्द्र . ग्रहेभ्यो नम” कहकर नीचे के चक्रानुसार क्रमशः नवग्रहों की गुरू
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.77)
- **Original**: भौम पंचोपचार पूजा तथा घोडश माताओं की भी पूजा करनी केतु
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.78)
- **Original**: राह चाहिए। षोडशमातृका मन्त्र: गौरी फा शची मेधा सावित्री विजया जया
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.79)
- **Original**: देवसेना स्वधा स्वाहा. मातरो लोकमात्तरः
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.80)
- **Original**: हृष्टि: पुष्टि: तथा तुष्टिरात्मनः कुलदेवता
- **Translation**: 

---

