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

### Verse 1 (Bramha 0.2821)
- **Original**: लगाये। पुन: पराभक्िकि साथ कमलसे तथा मुँहसे द्वादश यात्राकी प्रतिष्ठाकी विधि, पूजन, दान
- **Translation**: 

---

### Verse 2 (Bramha 0.2822)
- **Original**: विष्णुदेवतासम्बन्धी मल्लिका आदि अन्य पुष्पोंसे और फल सुनना चाहते हैं।
- **Translation**: 

---

### Verse 3 (Bramha 0.2823)
- **Original**: ओपुरुषोत्तमको पूजा करे। भोग और मोक्षके दाता खरह्माजी योले--ब्राह्मणो! जब बारह यात्राएँ
- **Translation**: 

---

### Verse 4 (Bramha 0.2824)
- **Original**: जगदीश्वर श्रीहरिकी इस प्रकार पूजा करके उनके पूरी हो जाये, तब विधिपूर्वक उनकी प्रतिष्ठा करे। ' समक्ष अगर, गूगल तथा अन्य सुगन्धित पदार्थोके
- **Translation**: 

---

### Verse 5 (Bramha 0.2825)
- **Original**: 138 » संक्षिप्त भ्रह्मपुराण * 2 00---.7> 00000... ुु.-.30 पपपेपपपपापप परतपफएरफ2फपे एन अप प पर क्‍।॑क्‍क्‍ाट साथ धूप जलाये। अपनी शक्तिके अनुसार घीसे
- **Translation**: 

---

### Verse 6 (Bramha 0.2826)
- **Original**: भगवान्‌की पूजाके बाद ब्राह्मणोंकी भी पूजा करे। दीपक जलाकर रखे, घी अथवा तिलके तेलसे
- **Translation**: 

---

### Verse 7 (Bramha 0.2827)
- **Original**: उनके लिये बारह गौएँ दान करके श्रद्धा और अन्य बारह दीपक जलाकर रखे। नैवेद्यके रूपमें
- **Translation**: 

---

### Verse 8 (Bramha 0.2828)
- **Original**: भक्तिपूर्वक सुवर्ण, छतरी और जूते, धन तथा बस्तर खीर, पूआ, पूड़ी, बड़ा, लड्डू, खाँड़ और फल
- **Translation**: 

---

### Verse 9 (Bramha 0.2829)
- **Original**: आदि समर्पित करे। सद्भावसे पूजित होनेपर भगवान्‌ निवेदन करे। इस प्रकार पश्ोपचारसे श्रीपुरुषोत्तमका
- **Translation**: 

---

### Verse 10 (Bramha 0.2830)
- **Original**: गोविन्द संतुष्ट होते हैं। आचार्यको भी भक्तिपूर्वक पूजन करके '3& नम: पुरुषोत्तमाय' इस मन्त्रका
- **Translation**: 

---

### Verse 11 (Bramha 0.2831)
- **Original**: गौ, वस्त्र, सुवर्ण, छतरी, जूते तथा काँसेका पात्र एक सौ आठ बार जप करे
- **Translation**: 

---

### Verse 12 (Bramha 0.2832)
- **Original**: इसके बाद भक्तिपूर्वक
- **Translation**: 

---

### Verse 13 (Bramha 0.2833)
- **Original**: अर्पित करे। तदनन्तर ब्राह्मणोंको खीर, पकवान, भगवान्‌ पुरुषोत्तमसे इस प्रकार प्रार्थना करें--
- **Translation**: 

---

### Verse 14 (Bramha 0.2834)
- **Original**: गुड़ और थीमें बने हुए पदार्थ भोजन कराये। जब नमस्ते. सर्वलोकेश . भक्तानामभयप्रद। वे भोजन करके तृप्त हो जाये, तब उनके लिये बारह संसारसागरे मगन॑ त्राहि मां पुरुषोत्तत
- **Translation**: 

---

### Verse 15 (Bramha 0.2835)
- **Original**: जलसे भरे हुए घट दान करे। उन घड़ोंके साथ यास्‍्ते भया कृता यात्रा द्वादशैव जगत्पते।
- **Translation**: 

---

### Verse 16 (Bramha 0.2836)
- **Original**: लड्डू और यथाशक्ति दक्षिणा भी होनी चाहिये। प्रसादात्तन गोविन्द सम्पूर्णास्ता भवन्तु मे
- **Translation**: 

---

### Verse 17 (Bramha 0.2837)
- **Original**: आचार्यकों भी कलश और दक्षिणा निवेदन करें। * भक्तोंको अभय प्रदान करनेवाले सर्वलोकेश्बर
- **Translation**: 

---

### Verse 18 (Bramha 0.2838)
- **Original**: इस तरह ब्राह्मणोंकी पूजा करके विष्णुतुल्य ज्ञानदाता पुरुषोत्तम ! आपको नमस्कार है। मैं इस संसार-सागरमें
- **Translation**: 

---

### Verse 19 (Bramha 0.2839)
- **Original**: गुरुकी भी पूर्ण भक्तिके साथ पूजा करे। पूजनके डूबा हुआ हूँ। मेरा उद्धार कीजिये। जगत्पते ! गोविन्द!
- **Translation**: 

---

### Verse 20 (Bramha 0.2840)
- **Original**: पश्चात्‌ नमस्कार करके यह मन्त्र पढ़े- आपके दर्शनके लिये मैंने जो यारहों यात्राएँ की हैं, , सर्वव्यापी जगन्नाथ: शड्खचक्रगदाधर:। ये सब आपके प्रसादसे मेरे लिये परिपूर्ण हों।' अनादिनिधतो देव: प्रीयतां पुरुषोत्तम:
- **Translation**: 

---

