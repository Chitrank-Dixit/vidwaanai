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

### Verse 1 (Narsihma Puran 0.4781)
- **Original**: 79 स सर्व दर्शयामास वासवोउन्त:पुरं तदा। ततो जगाद भूय: सा किंचिदगूढं मप स्थितप्‌
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.4782)
- **Original**: 80 विमुच्यैकां च॒ युवती सर्व ते दर्शित मया। इन्द जवाब सा रामा मन्दरे चास्ति अविज्ञाता सुरासुर:
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.4783)
- **Original**: 891 तां च ते दर्शयिष्यामि नाख्येयं कस्यच्चित्त्तया। जतः स॒ देबराजोउपि तबा सा्ध॑ च्व भुपते
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4784)
- **Original**: 82 गच्छल्नेवाम्बरे भूपष मन्दरं प्रति भूधरम्‌। तस्थ ते गच्छमानस्य विमानेनार्कबर्चंसा
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.4785)
- **Original**: 83 दर्शन॑ नारदस्यापि तस्य जात॑ तदाप्वरे। ते वीक्ष्य नारद॑ वीरो लज्ञमानो5पि वासव:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.4786)
- **Original**: 84 नमस्कृत्य जगादोच्चै: क्व यास्थसि महामुने। ततः कृताशी: स मुनिरवदत्त्रिदिवेश्वरम्‌
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.4787)
- **Original**: 85 गच्छामि मानसे स्त्रातुं देवराज सुखी भव। ताडीजड्डे उस्ति कुशल राक्षसानां महात्मनाम्‌
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.4788)
- **Original**: 86 श्रीतरसिंहपुराण ( अध्याय 63 उन दोनोके द्वाय यों कही जानेपर उस सुन्दरीने मधुर वाणीमें उत्तर दिया
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.4789)
- **Original**: 67--735,
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.4790)
- **Original**: नाडीजद्धा बोली--यदि देवराज इन्द्र स्वयं हो मेरे पास आयेंगे तो मैं उनकी बात मान सकतो हूँ; अन्यथा बिलकुल नहीं
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.4791)
- **Original**: तब अश्विनीकुमारोंने इन्द्रके पास जाकर उसका शुभ संदेश कहा
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.4792)
- **Original**: तब इन्द्र स्वयं आकर ओले--कृशाद्वि ! आज्ञा दो, मैं इस समय तुम्हारा कौन-सा कार्य करूँ? मैं सदाके लिये तुम्हारा दास हो गया हूँ; तुम जो कुछ माँगोगी, बह सब दूँगा
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.4793)
- **Original**: कुशाड्रीने कहा--ताथ! यदि आप मेरी माँगी हुई वस्तु अवश्य दे देंगे, तो नि:संदेह मैं आपको वशवर्तिनी हो जाऊँगी। आज आप अपनी समस्त भार्याओंको मुझे दिखाइये; देखूँ, आपकी कोई भी स्त्री मेरे रूपके सदुश है या नहीं ?
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.4794)
- **Original**: उसके यों कहनेपर इन्द्रने पुनः कहा--“'देवि! अआलो, मैं तुम्हें अपनी समस्त भार्याओंकों दिखाकँगा।'' यह कहकर इन्द्रने उसो समय उसे अपना सारा अन्त:पुर दिखाया। तब उस सुन्दरीने पुनः कहा--' अभी मुझसे कुछ छिपाया गया है। केवल एक युवतीकों छोड़कर और सब कुछ आपने दिखा दिया'
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.4795)
- **Original**: '79-801/,
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.4796)
- **Original**: इत्चने कहा--'“वह रमणी मन्दराचलपर है। देवता और असुर-किसोकों भी उसका पता नहीं है। मैं उसे भी तुम्हें दिखा दूँगा, परंतु यह रहस्य किसीपर प्रकर न करना।'” भूपाल! यह कहकर देवबराज इन्द्र उसके साथ आकाशमार्गसे मन्दराचलकी ओर चले। जिस समय वे सूर्पफेक समान कात्तिमान्‌ थिमानसे चणे जा रहे थे, उसी समय उन्हें आकाशमें देबर्षि नारदका दर्शन हुआ। नारदजीकों देखकर वीरवर इन्द्र यद्यपि लख्कति हुए, तथापि उन्हें नमस्कार करके पूछा--'महामुने! आप कहाँ जायेंगे ?'
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.4797)
- **Original**: 81--845,
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.4798)
- **Original**: तब सुनिवर नारदजोने आशीर्वाद देते हुए स्वर्गाधिपति इन्द्रसे कहा--देबराज! आप सुखी हों, मैं इस समय मानससरोवरपर ज्लान करने जा रहा हूँ।' [फिर उन्होंने नाडीजज्लाक्रों पहचानकर कहा-- ] “नाडीजलद्ले ! कहो तो महात्मा राक्षसरोंका कुशल तो है न?
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.4799)
- **Original**: अध्याय 63 ] विभीषणो5पि ते भ्राता सुखी तिष्ठति सर्वदा। एबमुक्ता चर मुनिना सा कृष्णवदनाभवत्‌
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.4800)
- **Original**: 87 विस्मितो देवराजो5पि छलितो दुष्टयानया। नारदो5पि गतः स््रातुं कैलासे मानस सर:
- **Translation**: 

---

