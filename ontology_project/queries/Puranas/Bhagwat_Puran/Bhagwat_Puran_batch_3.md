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

### Verse 1 (Bhagwat Puran 0.41)
- **Original**: आपके वचनोंसे मेरे दुःखकी भी बहुत कुछ शान्ति हो जायगी। मनुष्यका जब चड़ा भाग्य होता है, तभी आपके दर्शन हुआ करते हैं
- **Translation**: 

---

### Verse 2 (Bhagwat Puran 0.42)
- **Original**: नारदजी कहते हैं-तब मैंने उस ख्ोीसे पूछा--देवि ! तुम कौन हो? ये दोनों पुरुष तुम्हारे क्‍या होते हैं? और तुम्हारे पास ये कमलनयनों देवियाँ कौन हैं? तुम हमें विस्तारसे अपने दुःखका कारण
- **Translation**: 

---

### Verse 3 (Bhagwat Puran 0.43)
- **Original**: आ1] + ग्राहमत्य # ड्डे हा 7 भव ओ मिशेओ कक कक ओओ घ ओ पी पक कफ ऑ ऑआ ओ ओीऔ फओी की के के के के की ही के के के के के के के के के के औ के के हे औ हे हे औ हे औ औ हे हे औ क है कै औ है कै औ है के औ कौ ऑओ ओके के कै औ क कै! 'औ औ # औ औ औ कै औ है कै औ बताओ
- **Translation**: 

---

### Verse 4 (Bhagwat Puran 0.44)
- **Original**: युवतीने कहा--मेरा नाम भक्ति है, ये ज्ञान और वैसम्य नामक मेरे पुत्र हैं। समयके फेरसे ही ये ऐसे जर्जर हो गये हैं
- **Translation**: 

---

### Verse 5 (Bhagwat Puran 0.45)
- **Original**: ये देवियाँ गड्ाजी आदि नदियाँ हैं। ये सब मेरी सेवा करनेके लिये हो आयी हैं। इस प्रकार साक्षात्‌ देक्योके द्वारा सेवित होनेपर भी मुझे सुख-शान्ति नहां है
- **Translation**: 

---

### Verse 6 (Bhagwat Puran 0.46)
- **Original**: तपोधन ! अब ध्यान देकर मेरा वृत्तान्त सुनिये। मेरी कथा बैसे तो प्रसिद्ध है, फिर भी उसे सुनकर आप मुझे शान्ति प्रदान करें
- **Translation**: 

---

### Verse 7 (Bhagwat Puran 0.47)
- **Original**: मैं द्रतिड़ देशमें उत्पन्न हुई, कर्णाटकर्में बढ़ी, मुझको बुढ़ापेने आ घेरा
- **Translation**: 

---

### Verse 8 (Bhagwat Puran 0.48)
- **Original**: वहाँ घोर कलियुगके प्रभावसे पार्खाष्डियोने मुझे अद्भ-भड्ढ कर दिया। चिरकालतक यह अवस्था रहनेके कारण मैं अपने पुत्रोकि साध दुर्बल और निस्तेज हो गयी।
- **Translation**: 

---

### Verse 9 (Bhagwat Puran 0.49)
- **Original**: अब जबसे मैं वृन्दावन आयी, तबसे पुनः परम सुन्दरी सुरूपवती नवयुवती हो गयी हूँ। 50
- **Translation**: 

---

### Verse 10 (Bhagwat Puran 0.50)
- **Original**: किन्तु सामने पड़े हुए ये दोनों मेरे पुत्र थके-मंदि दुखी हो रहे है। अब में यह स्थान छोड़कर अन्यत्र जाना चाहती हूँ
- **Translation**: 

---

### Verse 11 (Bhagwat Puran 0.51)
- **Original**: ये दोनों बूढ़े हो गये हैं--इसी दुःखसे मैं दुःखी हूँ। मैं तरुणी क्यों और ये दोनों मेरे पुत्र बूढ़े क्यों ?
- **Translation**: 

---

### Verse 12 (Bhagwat Puran 0.52)
- **Original**: हम तीनों साथ-साथ रहनेवाले हैं। फिर यह विपरीतता क्यों? होना तो यह चाहिये कि माता बूढ़ी हो और पुत्र तरुण
- **Translation**: 

---

### Verse 13 (Bhagwat Puran 0.53)
- **Original**: इसीसे मैं आश्चर्यचकित चित्तसे अपनी इस्र अवस्थापर शोक करती रहती हूँ। आप परम बुद्धिमान्‌ एवं योगनिधि हैं; इसका क्या कारण हो सकता है, बताइये ?
- **Translation**: 

---

### Verse 14 (Bhagwat Puran 0.54)
- **Original**: नारदजीने कहा--साध्वि ! मैं अपने हृदयमें शन्दृष्टिसे तुस्हरे सम्पूर्ण दुःखका कारण देखता हैं, तुम्हें विषाद नहीं करना चाहिये। श्रीहरि तुम्हारा कल्याण करेंगे
- **Translation**: 

---

### Verse 15 (Bhagwat Puran 0.55)
- **Original**: सूतजी कहते हैं--मुनिबर नारदजीने एक क्षणमें ही उसका कारण जानकर कहा
- **Translation**: 

---

### Verse 16 (Bhagwat Puran 0.56)
- **Original**: नासदजीने कहा--देवि ! सावधान होकर सुनो। यह दारुण कलियुग है। इसीसे इस समय सदाचार, योगमार्ग और तप आदि सभी लुप्त हो गये हैं
- **Translation**: 

---

### Verse 17 (Bhagwat Puran 0.57)
- **Original**: लोग शठता और दुष्कर्ममें लगकर अघासुर बन रहे हैं। संसारमें जहाँ देखो, वहीं सत्पुरुष दुःखसे म्लान हैं और दुष्ट सुखी हो रहे हैं। इस समय जिस बुद्धिमान्‌ पुरुषका धैर्य बना रहे, वहो बड़ा ज्ञानी या पण्डित है
- **Translation**: 

---

### Verse 18 (Bhagwat Puran 0.58)
- **Original**: पृथ्वी क्रमशः प्रतिवर्ष शेषजीके लिये भाररूप होती जा रही है। अब यह छूनेयोम्य तो क्या, देखनेयोप्य भी नहीं रह गयी है और न इसमें कहीं मड्जल ही दिस्त्रायी देता है
- **Translation**: 

---

### Verse 19 (Bhagwat Puran 0.59)
- **Original**: अब किसोको पुत्रोंके साथ तुम्हारा दर्शन भी नहीं होता
- **Translation**: 

---

### Verse 20 (Bhagwat Puran 0.60)
- **Original**: विषयानुरागके कारण अंधे बने हुए जीवॉसे उपेक्षित होकर तुम जर्जर हो रही थी
- **Translation**: 

---

